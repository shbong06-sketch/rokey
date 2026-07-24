import rclpy
from rclpy.node import Node
from rclpy.qos import (QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy)
from std_msgs.msg import String
from rclpy.qos import qos_profile_sensor_data

class MapSubscription(Node):
    def __init__(self):
        super().__init__('map_subscriber')
        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=10,
        )
        self.create_subscription(String, 'map_info', self.recieve_cb , qos_profile_sensor_data)


    def recieve_cb(self, msg):
        self.get_logger().info(f"지도 수신 : {msg.data}")

def main():
    rclpy.init()
    rclpy.spin(MapSubscription())
    rclpy.shutdown()

if __name__=="__main__":
    main()