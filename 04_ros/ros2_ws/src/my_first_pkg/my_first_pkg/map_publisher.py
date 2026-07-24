# qos 객체 만들기
# 기본 구조 작성
# 발행
# 터미널에서 1차 확인
import rclpy
from rclpy.qos import (QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy)
from rclpy.node import Node
from std_msgs.msg import String
import time
from rclpy.qos import qos_profile_sensor_data

class MapPublisher(Node):
    def __init__(self):
        super().__init__('map_publisher')
        qos = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=10,
        )
        self.pub = self.create_publisher(String, 'map_info', qos_profile_sensor_data)
        self.create_timer(2.0, self.send_map)
        # self.send_map()     # TRANSIENT_LOCAL 확인해보기

    def send_map(self):
        msg = String()
        msg.data = f'map sending {str(time.time())}'
        self.pub.publish(msg)
        self.get_logger().info("-----맵 전달 중-----")
        pass


def main():
    rclpy.init()
    rclpy.spin(MapPublisher())
    rclpy.shutdown()

if __name__=="__main__":
    main()