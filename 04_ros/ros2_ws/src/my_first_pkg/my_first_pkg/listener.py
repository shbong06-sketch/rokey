import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.create_subscription(String, 'chatter', self.on_msg, 10)
    
    def on_msg(self, msg):
        self.get_logger().info('받음: ' + msg.data)

def main():
    rclpy.init()
    rclpy.spin(Listener())
    rclpy.shutdown()