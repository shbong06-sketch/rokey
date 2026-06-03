# week05_3.py

import pandas as pd

path = r"week\week05\대구광역시 동구_연도별 체납차량 번호판 영치실적_20251031.csv"
df_csv = pd.read_csv(path, encoding='cp949')
# 한국 공공데이터의 경우 'utf-8'이 아닐 가능성 높아 => 'cp949' or 'euc-kr' 해보기
df = pd.DataFrame(df_csv)
# print(df_csv)
print(df)


import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
plt.figure(figsize=(8, 5))

year = df['년도']
no_parked_vehicles = df['영치대수']
plt.plot(year, no_parked_vehicles, 'b-o', label='영치대수')

plt.xticks(df['년도'])  # 연도를 x축 눈금으로 설정
plt.title("대구광역시 동구 연도별 체납차량 번호판 영치실적")
plt.xlabel("년도")
plt.ylabel("영치대수")
plt.legend()    # 범례 표시
plt.grid(True)  # 격차 추가

plt.show()