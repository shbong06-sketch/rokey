import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

# 시방서
# 1. 타입 : Int32
# 2, 토픽명 : battery
# 3. 주기 : 2초
# 4. 값을 100에서 시작해서 2초마다 1씩 감소
# =======================================
# 노드 상속 받아서 커스텀 노드 구성
# publisher 생성
# timer 세팅 - 주기 2초
# 콜백 함수 만드는데, msg 생성하고, msg.data에 값을 넣고, 퍼블리셔로 publish
# 여기에서 1씩 줄어드는 걸 적용
# main 함수는 기본 구조 그냥 쓰기/입력만 수행

class BatteryPub(Node):
    def __init__(self):
        super().__init__('battery_pub')
        self.pub = self.create_publisher(Int32, 'battery', 10)
        self.create_timer(2.0, self.battery_callback)
        self.battery_level = 100

    def battery_callback(self):
        msg = Int32()
        msg.data = self.battery_level
        self.pub.publish(msg)
        self.get_logger().info(f'Battery: {msg.data} %')
        self.battery_level -= 1
        if self.battery_level <= 0 : self.battery_level = 0

def main():
    rclpy.init()
    node = BatteryPub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()