# opencv_inrange.py

import cv2
import numpy as np

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\candies.jpg')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# H(색조), S(채도), V(명도)
green_lower = np.array([35, 100, 100])
green_upper = np.array([85, 255, 255])

mask = cv2.inRange(hsv, green_lower, green_upper)

result = cv2.bitwise_and(image, image, mask=mask)

# 이미지 창에 표시
cv2.imshow("Green Color Filtering", result)
cv2.waitKey(0)  # 0: 무한 대기
cv2.destroyAllWindows()

# HSV 색 공간 구조
# HSV는 다음 세 가지 축으로 색을 표현

# 구성요소      의미                값 범위(OpenCV 기준)
# ----------------------------------------------
# H (Hue)        색상(0~179)         0~179
# S (Saturation) 채도(색의 선명함)   0~255
# V (Value)      명도(밝기)          0~255

# Hue(색상) 범위 기준표
# 색상          H 범위(대략적)      설명
# 빨강(Red)     0~10, 170~180      양쪽 끝에 걸쳐 있음
# 주황(Orange)  10~25
# 노랑(Yellow)  25~35
# 초록(Green)   35~85              => 현재 사용한 범위
# 파랑(Blue)    85~125 
# 남색(Navy)    125~145
# 보라(Purple)  145~170