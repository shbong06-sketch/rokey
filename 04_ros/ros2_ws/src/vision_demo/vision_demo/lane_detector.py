import rclpy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import numpy as np
import os
from rclpy.node import Node

class LaneDetector(Node):  # LaneDetector까지 진행
    '''
    1. 이미지 sub해서 띄우기
    2. 띄운 이미지를 Computer Vision 기술을 이용해서 차선 인식진행
    3. 자율주행을 위한 알고리즘으로 발전
    '''
    def __init__(self):
        super().__init__('lane_detector')
        self.bridge = CvBridge()
        self.create_subscription(Image, '/camera/image_raw', self.cb, 10)
        self.pub = self.create_publisher(Image, '/lane/overlay', 10)

    def cb(self, msg):  # frame(Image -> numpy. cv_bridge) 만들기. 이미지 영상 띄우기
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        # 흑백 -> 경계(Canny) -> ROI -> 직선(Hough) -> 원본이미지에 Overlay
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        h, w = edges.shape
        mask = np.zeros_like(edges)
        roi = np.array([[
                        (int(0.40 * w), int(0.375 * h)),  # TL
                        (int(0.60 * w), int(0.375 * h)),  # TR
                        (int(0.86 * w), int(1.00 * h)),   # BR
                        (int(0.14 * w), int(1.00 * h))    # BL
                    ]])
        cv2.fillPoly(mask, roi, 255)
        masked = cv2.bitwise_and(edges, mask)

        lines = cv2.HoughLinesP(masked, 1, np.pi/180, 50, minLineLength=40, maxLineGap=20)
        if lines is not None: # ⑤ 그리기
            for x1, y1, x2, y2 in lines[:, 0]:
                cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
        self.pub.publish(self.bridge.cv2_to_imgmsg(frame, 'bgr8'))

        # cv2.imshow('camera', frame)
        # cv2.imshow('camera', edges)
        # cv2.waitKey(1)


def main():
    rclpy.init()
    rclpy.spin(LaneDetector())
    rclpy.shutdown()

if __name__=="__main__":
    main()