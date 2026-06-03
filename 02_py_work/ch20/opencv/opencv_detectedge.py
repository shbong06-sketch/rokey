# opencv_detectedge.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\sample.jpg')

edges = cv2.Canny(image, threshold1=100, threshold2=200)
# edges = cv2.Canny(image, threshold1=10, threshold2=200)

# 이미지 창에 표시
cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)  # 0: 무한 대기
cv2.destroyAllWindows()

# 엣지(edge): 이미지에서 밝기(또는 색)가 갑자기 변하는 경계