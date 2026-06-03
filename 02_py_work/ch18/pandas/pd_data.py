# pd_data.py

import pandas as pd

## 데이터 분석
# 1. CSV 파일 데이터 읽기
path = r'ch18\pandas\data.csv'
df_csv = pd.read_csv(path)      # return 값 => DataFrame
# df_csv = pd.read_csv(path, header=None) # header에 대한 설정
print(type(df_csv))
print(df_csv)

print("----------------")
# Excel 파일 데이터 읽기
# path = r'ch18\pandas\data.xlsx'
# df_xl = pd.read_excel(path)
# print(type(df_xl))
# print(df_xl)

# excel 파일 구조
# book > sheet > cell

print("데이터 탐색---------------")
# print(df_csv.head())
print(df_csv.head(3))

print("----------------")
print(df_csv.tail())
# print(df_csv.tail(2))

print("----------------")
# 데이터 요약 정보
df_csv.info()

# 객체 타입
# 행 정보
# 열 정보
# (컬럼 번호, 컬럼명, 비어있지 않은 데이터 개수, 데이터 타입)
# 메모리

print("----------------")
# 기술 통계량 정보
print(df_csv.describe())

print("----------------")
# 랜덤 샘플링(개수 or 비율)
print(df_csv.sample(2))
print("----------------")
print(df_csv.sample(frac=0.5))

