# QoS에 대한 숙지 및 배열 인터페이스에 대한 연습
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data   # BEST_EFFORT / KEEP_LAST / depth '5' / VOLATILE
from sensor_msgs.msg import LaserScan

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        self.pub = self.create_publisher(LaserScan, 'scan', qos_profile_sensor_data)
        self.create_timer(1.0, self.tick_cb)
        self.get_logger().info(f"{'='*5}Start Sensor Publisher{'='*5}")

    def tick_cb(self):
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "ROKEY" + str(msg.header.stamp.sec)
        msg.ranges = [i for i in range(1,100+1)]
        self.pub.publish(msg)
        self.get_logger().info(f"스캔 발행 : {msg.header.stamp.sec}")
        pass

def main():
    rclpy.init()
    rclpy.spin(SensorPublisher())
    rclpy.shutdown()

if __name__=="__main__":
    main()
