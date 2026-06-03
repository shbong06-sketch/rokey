# pd_Series.py

import pandas as pd
# print(pd.__version__)     # 버전 확인

data = [10, 20, 30]
series = pd.Series(data)
# series = pd.Series(data, index=['a', 'b','c'])
# series = pd.Series()    # dtype: object -> 객체(제일 상단에 있는 자료형)
print(series)
print(type(series))

print("------------------------")
data = {'a': 10, 'b': 20, 'c': 30}
series1 = pd.Series(data)
print(series1)
