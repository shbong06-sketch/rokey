import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Heavy(Node):
    def __init__(self):
        super().__init__("heavy_pub")
        self.pub = self.create_publisher(String, "heavy", 10)
        self.msg = String(data='x'*1000000) # 1MB
        self.create_timer(1/30, self.tick)  # 30Hz

    def tick(self):
        self.pub.publish(self.msg)

def main():
    rclpy.init()
    rclpy.spin(Heavy())
    rclpy.shutdown()

if __name__=="__main__":
    main()