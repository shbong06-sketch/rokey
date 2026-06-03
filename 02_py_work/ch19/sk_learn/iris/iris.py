# iris.py
from sklearn.datasets import load_iris
import pandas as pd

### 데이터 수집 및 전처리
# 1. iris 데이터셋 로드
iris = load_iris()
# print(iris)

df = pd.DataFrame(data=iris.data,
                  columns=iris.feature_names)
df['target'] = iris.target  # 열 추가
# print(df.head())

# 0, 1, 2 로 표현된 label을 문자열로 활용
target_names = {
    0 : iris.target_names[0],   # 'setosa'
    1 : iris.target_names[1],   # 'versicolor'
    2 : iris.target_names[2]    # 'virginica'
}

df['target'] = df['target'].map(target_names)
print(df.head())

# 2. 필요한 열 추출하기
iris_data = df[['sepal length (cm)',
                'sepal width (cm)',
                'petal length (cm)',
                'petal width (cm)'
                ]]
iris_label = df['target']
print(iris_data)
print(iris_label)

from sklearn.model_selection import train_test_split
# 3. 학습 전용 데이터와 테스트 전용 데이터 분리
# 기본 분할 비율: 25% : 75%
train_data, test_data, train_label, test_label = \
    train_test_split(iris_data, iris_label)
# print(test_data)

# 4. 데이터 학습시키고 예측하기
from sklearn import svm
from sklearn import metrics

clf = svm.SVC()
clf.fit(train_data, train_label)

pre = clf.predict(test_data)

# 5. 정답률 확인
ac_score = metrics.accuracy_score(test_label, pre)
print(f"정답률 = {ac_score}")