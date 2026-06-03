# opencv_color.py
import cv2

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\sample.jpg')

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 3채널 -> 1채널
# rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # BGR => RGB ; (B <-> R)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # BGR => HSV

# 이미지 창에 표시
# cv2.imshow("Grayscaled image", gray)
# cv2.imshow("Grayscaled image", rgb)
cv2.imshow("Grayscaled image", hsv)
cv2.waitKey(0)  # 0: 무한 대기
cv2.destroyAllWindows()

# GRAY 방식
# 1채널만 사용(밝기만 표현) 255 흰색 ~ 0 검정
# 이미지 연산의 양을 줄여서 속도를 높이는데 필요
# 변환공식: Gray = 0.299 X R + 0.587 X G + 0.114 X B
# 채널 수 3개 => 1개 줄어듬

# HSV 방식
# RGB와 마찬가지로 3개의 채널을 갖는 색상 이미지 표현법
# 3채널은 H(Hue, 색조), S(Saturation, 채도), V(Value, 명도)
# 색을 한가지 채널에 넣어서, 색을 분리하거나 할 때 사용