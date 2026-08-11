import time
import psycopg2
import rclpy
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


def call(node, client, request, timeout=60.0):
    """서비스를 부르고 응답이 올 때까지 기다린다."""
    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future, timeout_sec=timeout)
    return future.result()          # 타임아웃이면 None


def main():
    # ── ROS 준비 ──────────────────────────────────────────
    rclpy.init()
    node = rclpy.create_node('mission_worker')
    log = node.get_logger()

    mode_cli = node.create_client(SetRobotMode, f'{SRV}/system/set_robot_mode')
    move_cli = node.create_client(MoveJoint,    f'{SRV}/motion/move_joint')

    while not move_cli.wait_for_service(timeout_sec=2.0):
        log.info('로봇 서비스 대기 중...')

    # 자율 모드 — "이제 프로그램이 명령한다"
    req = SetRobotMode.Request(); req.robot_mode = 1
    call(node, mode_cli, req)
    log.info('자율 모드 설정 완료')

    # ── DB 준비 ──────────────────────────────────────────
    conn = psycopg2.connect(host='localhost', port=5432,
                            dbname='robotdb', user='postgres',
                            password='robot1234')
    log.info('미션 워커 시작 — 큐를 지켜본다')

    # ── 큐 루프 ──────────────────────────────────────────
    while rclpy.ok():
        cur = conn.cursor()

        # ① 가장 급한 대기 미션 하나
        cur.execute("SELECT mission_id, kind, target FROM missions "
                    "WHERE status='대기' ORDER BY priority, created_at LIMIT 1;")
        row = cur.fetchone()
        if row is None:
            cur.close(); time.sleep(2.0); continue      # 큐가 비었다 — 2초 뒤 다시
        mission_id, kind, target = row

        # 모르는 목적지는 실패 처리 (움직이지 않는다)
        if target not in POSES:
            log.warn(f'미션 {mission_id}: 모르는 목적지 "{target}" → 실패 처리')
            cur.execute("UPDATE missions SET status='실패', finished_at=now() "
                        "WHERE mission_id=%s;", (mission_id,))
            conn.commit(); cur.close(); continue

        # ② 집는다 — WHERE status='대기' 가 이중 처리 방지
        cur.execute("UPDATE missions SET status='진행', started_at=now() "
                    "WHERE mission_id=%s AND status='대기';", (mission_id,))
        conn.commit()
        if cur.rowcount == 0:                            # 딴 워커가 먼저 집었다
            cur.close(); continue
        log.info(f'미션 {mission_id}: {kind} → {target}  실행')

        # ③ 로봇에게 — move_joint 서비스 호출
        req = MoveJoint.Request()
        req.pos = [float(v) for v in POSES[target]]
        req.vel = 30.0
        req.acc = 30.0
        res = call(node, move_cli, req)                  # 끝날 때까지 대기
        ok = bool(res and res.success)

        # ④ 기록한다
        cur.execute("UPDATE missions SET status=%s, finished_at=now() "
                    "WHERE mission_id=%s;",
                    ('완료' if ok else '실패', mission_id))
        conn.commit()
        log.info(f'미션 {mission_id} {"완료" if ok else "실패"}')
        cur.close()

    node.destroy_node(); rclpy.shutdown()


if __name__ == '__main__':
    main()
