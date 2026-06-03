# describe1.py
from scipy.stats import describe

data = [1, 2, 3, 4, 5, 6, 7]

stats = describe(data)
print(stats)

# 평균(중심), 분산(퍼짐 정도), 외도/첨도(분포의 형태)
# 외도(Skewness): 분포의 비대칭 정도
# 첨도(Kurtosis): 분포의 뽀족한 정도