# 시방서
# 1. 타입 : Float32
# 2, 토픽명 : speed
# 3. 주기 : 0.5초
# 4. 값을 받아서,
    # battery_level이 20보다 작아지면 경고 메시지를 로그로 출력
    # 0이 되면 시스템 멈췄다고 이야기 해주기
# =======================================
# 노드 상속 받아서 커스텀 노드 구성
# subscriber 생성
# 콜백 함수
# 수신된 배터리 값에 따라 분기 -> 20 이상 / 20~0 / 0 인 상황 별 메시지 출력
# main 함수는 기본 구조 그냥 쓰기/입력만 수행

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SpeedSub(Node):
    def __init__(self):
        super().__init__('speed_sub')
        self.create_subscription(Int32, 'speed', self.speed_callback, 10)

    def speed_callback(self, msg):
        speed = msg.data
        if speed > 50:
            self.get_logger().error(f'Speed is too high ({speed} km/h). Slow down!')
        
        elif speed >= 25:
            self.get_logger().warning(f'Speed is high ({speed} km/h).')

        else:
            self.get_logger().info(f'Speed : {speed} km/h.')

def main():
    rclpy.init()
    node = SpeedSub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()