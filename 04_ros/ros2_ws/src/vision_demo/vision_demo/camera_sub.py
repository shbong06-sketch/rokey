import rclpy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import numpy as np
import os
from rclpy.node import Node

class CameraSub(Node):
    '''
    이미지 sub해서 띄우기
    '''
    def __init__(self):
        super().__init__('lane_detector')
        self.bridge = CvBridge()
        self.create_subscription(Image, '/camera/image_raw', self.cb, 10)

    def cb(self, msg):  # frame(Image -> numpy. cv_bridge) 만들기. 이미지 영상 띄우기
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        
        cv2.imshow('camera', frame)
        cv2.waitKey(1)

def main():
    rclpy.init()
    rclpy.spin(CameraSub())
    rclpy.shutdown()

if __name__=="__main__":
    main()