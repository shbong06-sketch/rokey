import os
import time
import psycopg2
import rclpy
import dotenv
from rclpy.node import Node
from dsr_msgs2.srv import MoveJoint, SetRobotMode

# ── 목적지 이름 → 관절 자세(도) ────────────────────────────
# DB 는 "어디로"(이름)만 알고, "어떻게"(자세)는 노드가 안다.
POSES = {
    '대기장소': [0.0,   0.0,  0.0, 0.0,  0.0, 0.0],
    '선반A':    [0.0,   0.0, 90.0, 0.0, 90.0, 0.0],
    '선반B':    [30.0,  0.0, 90.0, 0.0, 90.0, 0.0],
    '충전독':   [-30.0, 30.0, 60.0, 0.0, 90.0, 0.0],
}

SRV = '/dsr01/dsr_controller2'

class MissionWorker(Node):
    def __init__(self):
        super().__init__('mission_worker')
        self.log = self.get_logger()
        # ROS 준비
        self.mode_cli = self.create_client(SetRobotMode, f'{SRV}/system/set_robot_mode')
        self.move_cli = self.create_client(MoveJoint,    f'{SRV}/motion/move_joint')

        while not self.move_cli.wait_for_service(timeout_sec=2.0):
            self.log.info('로봇 서비스 대기 중...')

        # 자율 모드 — "이제 프로그램이 명령한다"
        req = SetRobotMode.Request()
        req.robot_mode = 1
        self.call(self.mode_cli, req)
        self.log.info('자율 모드 설정 완료')

        # DB 준비 — 시크릿은 코드가 아니라 .env 가 알려준다
        self.conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'localhost'),
            port=os.environ.get('DB_PORT', '5432'),
            dbname=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
        )
        self.log.info('미션 워커 시작 — 큐를 지켜본다')

    def call(self, client, request, timeout=60.0):
        """서비스를 부르고 응답이 올 때까지 기다린다."""
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future, timeout_sec=timeout)
        return future.result()          # 타임아웃이면 None

    def spin(self):
        # 큐 루프 — 미션이 생길 때마다 실행한다.
        while rclpy.ok():
            cur = self.conn.cursor()

            # ① 가장 급한 대기 미션 하나
            cur.execute("SELECT mission_id, kind, target FROM missions "
                        "WHERE status='대기' ORDER BY priority, created_at LIMIT 1;")
            row = cur.fetchone()
            if row is None:
                cur.close()
                time.sleep(2.0)
                # 큐가 비었다 — 2초 뒤 다시
                continue
            mission_id, kind, target = row

            # 모르는 목적지는 실패 처리 (움직이지 않는다)
            if target not in POSES:
                self.log.warn(f'미션 {mission_id}: 모르는 목적지 "{target}" → 실패 처리')
                cur.execute("UPDATE missions SET status='실패', finished_at=now() "
                            "WHERE mission_id=%s;", (mission_id,))
                self.conn.commit()
                cur.close()
                continue

            # ② 집는다 — WHERE status='대기' 가 이중 처리 방지
            cur.execute("UPDATE missions SET status='진행', started_at=now() "
                        "WHERE mission_id=%s AND status='대기';", (mission_id,))
            self.conn.commit()
            if cur.rowcount == 0:       # 딴 워커가 먼저 집었다
                cur.close()
                continue
            self.log.info(f'미션 {mission_id}: {kind} → {target}  실행')

            # ③ 로봇에게 — move_joint 서비스 호출
            req = MoveJoint.Request()
            req.pos = [float(v) for v in POSES[target]]
            req.vel = 30.0
            req.acc = 30.0
            res = self.call(self.move_cli, req)     # 끝날 때까지 대기
            ok = bool(res and res.success)

            # ④ 기록한다
            cur.execute("UPDATE missions SET status=%s, finished_at=now() "
                        "WHERE mission_id=%s;",
                        ('완료' if ok else '실패', mission_id))
            self.conn.commit()
            self.log.info(f'미션 {mission_id} {"완료" if ok else "실패"}')
            cur.close()

    def destroy_node(self):
        self.conn.close()
        super().destroy_node()


def main(args=None):
    dotenv.load_dotenv()
    required = ['DB_NAME', 'DB_USER', 'DB_PASSWORD']
    missing = [k for k in required if not os.environ.get(k)]
    if missing:
        raise SystemExit(f'.env 에 누락된 값: {", ".join(missing)}')

    rclpy.init(args=args)
    worker = MissionWorker()
    worker.spin()
    worker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
