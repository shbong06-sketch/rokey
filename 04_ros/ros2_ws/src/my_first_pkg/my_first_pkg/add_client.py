import rclpy
from rclpy.node import Node
# 우리가 만든 interface 중 AddTwoInts 를 import 한다.
from my_interfaces.srv import AddTwoInts

# 클라이언트 노드
# 1. 어떤 노드에서 상시 작업을 수행하다가, 서비스 요청을 시도할 수 있다.
# 2. 한번의 요청을 시도하는 노드
# cf. ros2 service call /add_two_ints my_interfaces/srv/AddTwoInts "{num1: 10, num2: 20}"

class AddClient(Node):
    def __init__(self):
        super().__init__('add_client')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for Server")
        req = AddTwoInts.Request()
        req.num1 = 3
        req.num2 = 4
        self.future = self.cli.call_async(req)

        self.get_logger().info(f"Send Request to Server: {req.num1} + {req.num2}")

    # ros2 service call /add_two_ints my_interfaces/srv/AddTwoInts "{num1: 3, num2: 5}"

def main(args=None):
    rclpy.init(args=args)
    node = AddClient()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()