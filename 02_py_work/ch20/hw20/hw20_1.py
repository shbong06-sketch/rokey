# hw20_1.py

# 6.
# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# # 1. 샘플 데이터 셋 로드
# arr = np.random.normal(50, 10, 1000)
# # 2. 기본 스타일 설정
# sns.set_theme(style='dark', palette='muted')
# # 3. 그래프 표시
# sns.histplot(data=arr, kde=True)
# plt.show()

# 7.
# import seaborn as sns
# import matplotlib.pyplot as plt

# # 1. 샘플 데이터셋 로드
# tips = sns.load_dataset("tips")
# # 2. 기본 스타일 설정
# sns.set_theme(style='darkgrid', palette='colorblind')
# # 3. 그래프 표시
# sns.boxplot(data =tips,
#             x= 'day',
#             y='total_bill')
# plt.show()

# 8.
# import cv2
# # 1. 이미지 파일 읽기
# image = cv2.imread(r'ch20\hw20\people.jpg')
# # 2. 이미지 출력
# cv2.imshow("Loaded image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 9.
# import cv2
# # 1. 이미지 파일 읽기
# image = cv2.imread(r'ch20\hw20\people.jpg')
# # 2. 이미지 흑백으로 변환
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # 3. 이미지 출력
# cv2.imshow("Gray image", gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 10.
import cv2
# 1. 이미지 파일 읽기
image = cv2.imread(r'ch20\hw20\people.jpg')
# 2. 이미지의 엣지 감지
edges = cv2.Canny(image, threshold1=180, threshold2=200)

# 3. 이미지 출력
cv2.imshow("Edged image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()