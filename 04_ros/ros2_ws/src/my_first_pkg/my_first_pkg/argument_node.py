# argument_node 만들기
# 1. 상속 - Node
# 2. pub 생성 - create_publisher(메시지타입, '토픽명', 버퍼)
# 3. timer 구성 - 몇 초, 콜백
# 4. 콜백함수 - a, b 값 랜덤 생성 -> 송출 -> 로그로 출력
# 5. main 돌리기 - 병렬 필요? no

import rclpy
from rclpy.node import Node
from my_interfaces.msg import ArithmeticArgument
import random

class Argument(Node):
    def __init__(self):
        super().__init__('argument')
        self.pub = self.create_publisher(ArithmeticArgument, 'arithmetic/argument', 10)
        self.create_timer(1.0, self.tick)

    def tick(self):
        msg = ArithmeticArgument()
        msg.argument_a = random.uniform(0.0, 9.0)
        msg.argument_b = random.uniform(0.0, 9.0)
        self.pub.publish(msg)
        self.get_logger().info(f"a={msg.argument_a:.1f} b={msg.argument_b:.1f}")

def main():
    rclpy.init()
    node = Argument()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()