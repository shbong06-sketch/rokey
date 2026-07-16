import rclpy, time
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup

class BlockingFixed(Node):
    def __init__(self):
        super().__init__('blocking_fixed')
        grp = ReentrantCallbackGroup()      # 동시 실행 지원 그룹
        # 두 개의 타이머를 같은 콜백 그룹에 넣는다.
        self.create_timer(0.5, self.fast, callback_group=grp)
        self.create_timer(1.0, self.slow, callback_group=grp)

    def fast(self):
        self.get_logger().info('fast')

    def slow(self):
        time.sleep(3.0)
        self.get_logger().info('slow 끝')

def main():
    rclpy.init()
    node = BlockingFixed()
    ex = MultiThreadedExecutor()    # rclpy.spin(node) 대신 executor를 만들어 spin()
    ex.add_node(node)
    ex.spin()
    rclpy.shutdown()