# opencv_detectObj.py
import cv2

# 1. 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\people.jpg')

# 2. 얼굴 검출을 위한 모델 확인
# 'haarcascade_eye.xml'
# 'haarcascade_russian_plate_number.xml'
# haarcascade_car.xml'
face_path = cv2.data.haarcascades + \
    'haarcascade_frontalface_default.xml'

# 3. 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 4. 케스케이스 분류기 생성
face_cascade = cv2.CascadeClassifier(face_path)

faces = face_cascade.detectMultiScale(
    gray,                # 입력 이미지(그레이스케일)
    scaleFactor=1.1,     # 이미지 크기를 줄여가며 검출(1.1배씩 감소 = 10%씩 줄여가며 검사)
                         # 얼굴 크기는 사람마다 다르므로 이미지를 축소하면서 얼굴을 탐색
    minNeighbors=5,      # 객체로 인지되기 위한 최소 중복 검출 수
                         # 보통 4~6 정도가 안정적
    minSize=(20,20),     # 최소 객체 크기 => 이보다 작은 객체는 얼굴로 간주 않음
    maxSize=(200,200)    # 최대 객체 크기 => 이보다 큰 객체는 얼굴로 간주 않음
    )
print(faces)    # [x, y, w, h]

# 5. 검출된 객체에 사각형 표시
for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h), (200, 0, 0), 2)

# 6. 이미지 창에 표시
cv2.imshow("Face Detection", image)
cv2.waitKey(0)  # 0: 무한 대기
cv2.destroyAllWindows()

# 정면 얼굴에서 자주 나타나는 밝기 패턴을 단계적으로 검사해서 얼굴인지 판단
# => "얼굴이라면 이런 패턴이어야 한다."
# 예) 눈 주변: 어두움, 코/볼: 밝다 ...
# 단계적 검출 기준을 가짐: 눈 -> 코 -> 얼굴 대칭 -> ...