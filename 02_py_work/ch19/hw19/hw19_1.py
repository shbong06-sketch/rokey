# hw19_1.py

# # 6.
# import statsmodels.api as sm

# X = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# X2 = sm.add_constant(X)

# model = sm.OLS(y, X2).fit()
# # print(model.summary())
# print("기울기:", model.params[1])
# print("절편:", model.params[0])

# print("------------------------------")
# # 7.
# import matplotlib.pyplot as plt

# plt.plot(X, model.predict(X2), color='r')
# plt.scatter(X, y)
# plt.title("Linear Regression")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

# print("------------------------------")
# # 8.
# from sklearn import svm
# from sklearn import metrics
# import pandas as pd

# # 1. 데이터 수집 및 전처리
# X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# # 2. 알고리즘 선택 및 학습
# clf = svm.SVC().fit(X, y)

# # 3. 예측
# pre = clf.predict([[4.5], [6.5]])
# print(pre)

print("------------------------------")
# 9.
from scipy.optimize import root

def equation(x):
    return (x-3)**2

sol = root(equation, x0=1)
print(sol.x)

print("------------------------------")
# 10.
from scipy.stats import describe

group_A = [80, 85, 90, 75, 95]
stats = describe(group_A)
print(stats)