import rclpy
from rclpy.node import Node
from std_msgs.msg import String

'''
timer가 시간될 때마다, tick 메서드 실행
  tick 메서드 내부 -> pub에게 msg를 보내도록 반복시키는 구조
'''

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(String, 'chatter', 10)
        self.create_timer(1.0, self.tick)

    def tick(self):
        msg = String()
        msg.data = 'Hello, ROS 2!'
        self.pub.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    talker = Talker()
    rclpy.spin(talker)
    talker.destroy_node()
    rclpy.shutdown()