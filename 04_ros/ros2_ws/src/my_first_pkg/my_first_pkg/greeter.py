import rclpy
from rclpy.node import Node

class Greeter(Node):
    def __init__(self):
        super().__init__('greeter')
        self.declare_parameter('who', 'world')  # {key: value}
        self.create_timer(1.0, self.tick)
        self.n = 0

    def tick(self):
        who = self.get_parameter('who').value
        self.get_logger().info(f'Hello, {who}! : {str(self.n)}')
        self.n += 1

def main():
    rclpy.init()
    node = Greeter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

