# xor_train2.py
from sklearn import svm     # 알고리즘
from sklearn import metrics # 평가
import pandas as pd         # 데이터 분석 및 조작

# 1. 데이터 수집 및 전처리
xor_data = [
    # P, Q result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
# 데이터 가공 => 학습 데이터와 학습 레이블 분리
xor_df = pd.DataFrame(xor_data)

# 학습 데이터 (독립 변수)
# data = xor_df.loc[행, 열] => 데이터 가져오기
data = xor_df.loc[:, 0:1]
# print(data)

# 학습 레이블(정답) (종속 변수)
label = xor_df.loc[:, 2]
print(label)

# 2. 알고리즘 선택
clf = svm.SVC()   # 분류 알고리즘

# 3. 학습/훈련 => 모델 생성
# fit(학습데이터, 학습레이블)
clf.fit(data, label)

# 4. 예측
pre = clf.predict(data)
print(pre)

# 5. 정확도 평가
ac_score = metrics.accuracy_score(label, pre)
print(f"정답률: {ac_score}")