# 시방서
# 1. 타입 : Int32
# 2, 토픽명 : battery
# 3. 주기 : 2초
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

class BatterySub(Node):
    def __init__(self):
        super().__init__('battery_sub')
        self.create_subscription(Int32, 'battery', self.battery_callback, 10)

    def battery_callback(self, msg):
        battery_level = msg.data
        if battery_level <= 0:
            self.get_logger().error(f'Battery level is ({battery_level})%. System stopped.')
        
        elif battery_level < 20:
            self.get_logger().warn(f'Warning: Battery level is low ({battery_level}% remained.)')

        else:
            self.get_logger().info(f'Battery level : {battery_level}%')

def main():
    rclpy.init()
    node = BatterySub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()