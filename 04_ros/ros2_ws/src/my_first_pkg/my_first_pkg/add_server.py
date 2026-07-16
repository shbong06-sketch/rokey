import rclpy
from rclpy.node import Node
# 우리가 만든 interface 중 AddTwoInts 를 import 한다.
from my_interfaces.srv import AddTwoInts

class AddServer(Node):
    def __init__(self):
        super().__init__('add_server')
        # add two ints라는 이름으로 서비스를 생성
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        # 요청으로 들어온 두 정수를 더해서 응답에 넣어준다.
        response.sum = request.num1 + request.num2
        self.get_logger().info(f'Incoming request: num1={request.num1}, num2={request.num2}, sum={response.sum}')
        return response
    
def main(args=None):
    rclpy.init(args=args)
    node = AddServer()
    rclpy.spin(node)
    rclpy.shutdown()