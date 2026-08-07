import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py.point_cloud2 import read_points_numpy
import numpy as np

class CloudSub(Node):
    def __init__(self):
        super().__init__('cloud_sub')
        self.create_subscription(PointCloud2, '/points', self.cb, 10)

    def cb(self, msg):   # 메시지 잘 들어오나, numpy로 잘 바뀌나?
        xyz = read_points_numpy(msg, field_names=['x','y','z'], skip_nans=True)
        self.get_logger().info(f"넘어온 점의 개수: {len(xyz)}")


def main():
    rclpy.init()
    rclpy.spin(CloudSub())
    rclpy.shutdown()


if __name__=="__main__":
    main()