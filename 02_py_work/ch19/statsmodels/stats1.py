# stats1.py

import statsmodels.api as sm

# data1 = sm.datasets.get_rdataset("mtcars")
# data = data1.data
data = sm.datasets.get_rdataset("mtcars").data
# print(data)
# print(type(data))   # pandas.DataFrame
print(data.head())

X = data['hp']      # 마력
y = data['mpg']     # 연비

# 상수항 추가
X = sm.add_constant(X)


# X 대문자 표시는 통계/머신러닝에서 독립변수 표현 관례
# y 소문자 표시는 종속변수 표현 관례
# 베타: 계수, 입실론 : 오차

# 모델 생성 및 학습
# ols = sm.OLS()
# ols.fit()
model = sm.OLS(y, X).fit()

# 평가
print(model.summary())

print("모델 계수-----------")
print(model.params)
print(model.params['hp'])       # 기울기
print(model.params['const'])    # 절편