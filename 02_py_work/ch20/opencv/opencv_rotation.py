# opencv_rotation.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\sample.jpg')

print(image.shape)      # 세로, 가로, 채널
(h, w) = image.shape[0:2]
center = (w//2, h//2)

# 1. 회전 행렬 생성
M = cv2.getRotationMatrix2D(center, 45, 1.0)

# 2. 실제 변환 적용
rotated = cv2.warpAffine(image, M, (w,h))

# 이미지 창에 표시
cv2.imshow("Rotated image", rotated)
cv2.waitKey(0)  # 0: 무한 대기
cv2.destroyAllWindows()