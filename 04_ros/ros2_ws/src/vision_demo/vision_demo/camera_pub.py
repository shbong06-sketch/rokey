import rclpy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import numpy as np
import os
from rclpy.node import Node

# lane.mp4에서 영상을 받아서 pub하는게 목적

class CameraPub(Node):
    def __init__(self):
        super().__init__('camera_publisher')
        self.pub = self.create_publisher(Image, '/camera/image_raw', 10)
        self.bridge = CvBridge()
        # lane.mp4 영상을 cv2를 통해서 image를 받는 것
        # 영상 파일 경로 설정 -> cap = cv2.VideoCapture() -> cap.read()
        self.video_path = '/home/shbong/worksapce/rokey/rokey/04_ros/ros2_ws/lane.mp4'    # os.path.join()
        self.cap = cv2.VideoCapture(self.video_path)
        self.fps = 10
        self.create_timer(1/self.fps, self.tick)

    def tick(self):
        # 영상을 하나씩 read => publish
        if not self.cap.isOpened():
            self.get_logger().warn("VideoCapture 실패")
            return

        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().info('영상 끝에 도달하여 처음부터 다시 재생합니다.')
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()
            if not ret:
                self.get_logger().warn('영상 재생 실패')
                return

        msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'camera'
        self.pub.publish(msg)

def main():
    rclpy.init()
    rclpy.spin(CameraPub())
    rclpy.shutdown()

if __name__=="__main__":
    main()