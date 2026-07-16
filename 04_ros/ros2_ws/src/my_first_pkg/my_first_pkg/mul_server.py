import rclpy
from rclpy.node import Node
from my_interfaces.srv import Multiply

class MultiplyServer(Node):
    def __init__(self):
        super().__init__('multiply_server')
        self.srv = self.create_service(Multiply, 'multiply_server', self.multiply_callback)

    def multiply_callback(self, request, response):
        response.result = request.num1 * request.num2
        self.get_logger().info(f'Incoming request: num1={request.num1}, num2={request.num2}, result={response.result}')
        return response
    
def main(args=None):
    rclpy.init(args=args)
    node = MultiplyServer()
    rclpy.spin(node)
    rclpy.shutdown()
