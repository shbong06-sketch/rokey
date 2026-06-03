# opencv_module.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\sample.jpg')

# 이미지 창에 표시
cv2.imshow("Loaded image", image)
cv2.waitKey(0)  # 0: 무한 대기
cv2.destroyAllWindows()