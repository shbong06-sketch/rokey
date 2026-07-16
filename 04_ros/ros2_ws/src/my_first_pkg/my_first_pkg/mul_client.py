import rclpy
from rclpy.node import Node
from my_interfaces.srv import Multiply

class MultiplyClient(Node):
    def __init__(self):
        super().__init__('multiply_client')
        self.cli = self.create_client(Multiply, 'multiply_server')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('서버 대기 중...')
        req = Multiply.Request()
        req.num1 = 3
        req.num2 = 4
        self.future = self.cli.call_async(req)
        self.get_logger().info(f'서버에 요청 전송: {req.num1} * {req.num2}')

def main(args=None):
    rclpy.init(args=args)
    node = MultiplyClient()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
