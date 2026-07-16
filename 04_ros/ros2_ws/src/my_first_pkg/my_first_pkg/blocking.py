import rclpy, time
from rclpy.node import Node

class Blocking(Node):
    def __init__(self):
        super().__init__('blocking')
        self.create_timer(0.5, self.fast)   # 0.5초마다
        self.create_timer(1.0, self.slow)   # 1초마다

    def fast(self):
        self.get_logger().info('fast')

    def slow(self):
        time.sleep(3.0)                     # 3초 붙잡는다. 실제론 무거운 계산, 통신 등이 해당 위치에 온다.
        self.get_logger().info('slow 끝')

def main():
    rclpy.init()
    rclpy.spin(Blocking())
    rclpy.shutdown()