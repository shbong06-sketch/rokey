# xor.py

# import sklearn as sk
from sklearn import svm     # 알고리즘
from sklearn import metrics # 평가

# 1. 데이터 수집 및 전처리 -> 직접 데이터를 넣어서 생략

# 2. 알고리즘 선택
clf = svm.SVC()   # 분류 알고리즘

# 3. 학습/훈련 => 모델 생성
# fit(학습데이터, 학습레이블)
clf.fit(
    [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ],
    [0, 1, 1, 0]
)

# 4. 예측
pre = clf.predict(
    [[0, 1], [1, 1]]
)
print(pre)

# 5. 정확도 평가
ac_score = metrics.accuracy_score([1,0], pre)
print(f"정답률: {ac_score}")