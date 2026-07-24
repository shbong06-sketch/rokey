import rclpy
from rclpy.node import Node
from patrol_interfaces.msg import RobotStatus
from patrol_interfaces.srv import Command
from patrol_interfaces.action import Patrol
from rclpy.action import ActionServer
import time

class Robot(Node):
    def __init__(self):
        super().__init__('robot_node')
        self.declare_parameter('period', 1.0)
        p = self.get_parameter('period').value
        # pub 생성, p 시간 간격으로 송출
        self.pub = self.create_publisher(RobotStatus, 'robot/status', 10)
        # 타이머 생성
        self.create_timer(p, self.report)
        # 명령 서비스 서버
        self.create_service(Command, 'robot/command', self.on_cmd)
        # 액션 서버
        self.act = ActionServer(self, Patrol, 'robot/patrol', self.patrol)

    def report(self):
        # p 시간마다, 로봇의 상태를 송출
        msg = RobotStatus()
        msg.battery = 81.5      # 실전에서는 센서를 달아서, 실제 값을 받아 전달
        msg.position = 'B-17'   # SLAM과 연결해 현재의 위치를 파악해 보내준다. -> 관제 노드에서 해당 위치 좌표 기반으로 현재 위치(구역) 파악
        self.pub.publish(msg)

    # 콜백함수가 Node에서 호출될 때 받는 인자의 개수가 다르다.
    # 토픽 -> pub 콜백(0), sub 콜백(msg)
    # 서비스 -> req, res
    # 액션 -> goal_handler

    def on_cmd(self, request, response):
        # 받은 명령 : F-12 출력되도록
        self.get_logger().info(f"받은 명령 : {request.order}")
        response.accepted = True
        return response

    # 액션
    # - 몇 바퀴 순찰 (요청/목표 받아서) -> 1바퀴째, 멈칫, 2바퀴째, 멈칫, ... -> 완료
    def patrol(self, goal_handler):
        # goal을 받고 (몇 바퀴 돌지?)
        mission_laps = goal_handler.request.laps
        # 처리하며 피드백 (n바퀴 순찰하면서 'n번째 순찰 중' 보고)
        fb = Patrol.Feedback()
        for i in range(mission_laps):
            fb.progress = i + 1     # 1바퀴, 2바퀴, ...
            goal_handler.publish_feedback(fb)
            time.sleep(2.0)
            self.get_logger().info(f"현재 {mission_laps}번 중 {i+1}번째 순찰 중.")
        # 결과를 응답 ('근무 완료!' 응답)
        goal_handler.succeed()
        result = Patrol.Result()
        result.done = True
        return result

def main():
    rclpy.init()
    rclpy.spin(Robot())
    rclpy.shutdown()

if __name__ == "__main__":
    main()