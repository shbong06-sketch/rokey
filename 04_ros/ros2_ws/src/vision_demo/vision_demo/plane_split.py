import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py.point_cloud2 import read_points_numpy
import numpy as np
import open3d as o3d
from sensor_msgs_py import point_cloud2
from std_msgs.msg import Header

# 바닥과 물체가 감지된 point cloud 정보를 받기
# 여기에서 바닥을 제외한 물체 부분만 추출
# 물체 부분에 대한 point cloud를 pub -> rviz로 확인

class CloudSub(Node):
    def __init__(self):
        super().__init__('cloud_sub')
        self.create_subscription(PointCloud2, '/points', self.cb, 10)
        self.pub = self.create_publisher(PointCloud2, '/points/objects', 10)
        
    def cb(self, msg):   # 메시지 잘 들어오나, numpy로 잘 바뀌나?
        xyz = read_points_numpy(msg, field_names=['x','y','z'], skip_nans=True)
        # self.get_logger().info(f"넘어온 점의 개수: {len(xyz)}")
        # xyz(numpy) -> pcd(open3d)
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(xyz)

        # 다운샘플링 5cm 격자로 다운샘플
        pcd = pcd.voxel_down_sample(0.05)

        # 평면을 검출(RANSAC)
        plane, inliers = pcd.segment_plane(distance_threshold=0.05, ransac_n=3, num_iterations=1000)
        ground = pcd.select_by_index(inliers)   # 바닥 점들 검출
        objects = pcd.select_by_index(inliers, invert=True)  # 바닥을 제외한 물체 검출
        self.get_logger().info(f"ground 점의 개수: {len(ground.points)} == objects 점의 개수: {len(objects.points)}")

        # 발행 : array -> PointsCloud2
        pts = np.array(objects.points)
        header = Header()
        header.stamp = self.get_clock().now().to_msg()
        header.frame_id = 'map'
        
        # RViz Fixed Frame
        msg = point_cloud2.create_cloud_xyz32(header=header, points=pts)
        self.pub.publish(msg)
        self.get_logger().info(f"발행 : {len(pts)} 점")

def main():
    rclpy.init()
    rclpy.spin(CloudSub())
    rclpy.shutdown()


if __name__=="__main__":
    main()