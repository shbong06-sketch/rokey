# opencv_video.py

import cv2

# cap = cv2.VideoCapture(0)   # 웹캠 사용
cap = cv2.VideoCapture(r'ch20\opencv\turtle.mp4')

while True:
    # 이미지 파일 읽기
    ret, frame = cap.read()
    if not ret:
        break

    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow("Loaded image", edges)

    # 키보드로 입력되는 키를 인식하여 정수값 반환
    if cv2.waitKey(10) == ord('q'):    # 대기시간(ms)
        break


cap.release()               # 비디오 장치 사용 후 자원을 해제
cv2.destroyAllWindows()     # 모든 OpenCV 창 닫기