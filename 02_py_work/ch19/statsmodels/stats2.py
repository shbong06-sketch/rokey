# stats1.py

import statsmodels.api as sm

# data1 = sm.datasets.get_rdataset("mtcars")
# data = data1.data
data = sm.datasets.get_rdataset("mtcars").data
# print(data)
# print(type(data))   # pandas.DataFrame
print(data.head())

X = data[['hp', 'wt']]  # 마력 중량
y = data['mpg']         # 연비

# 상수항 추가
X = sm.add_constant(X)

# 모델 생성 및 학습
# ols = sm.OLS()
# ols.fit()
model = sm.OLS(y, X).fit()

print(model.summary())

print("모델 계수-----------")
print(model.params)
print(model.params['hp'])       # 기울기
print(model.params['wt'])       # 기울기
print(model.params['const'])    # 절편