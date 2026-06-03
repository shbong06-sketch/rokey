# pd_data1.py
import pandas as pd

## 데이터 조작
print("------------------")
# 딕셔너리 활용 생성
data = {
    'ID' : [1, 2, 3],
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [30, 35, 25]
}
df = pd.DataFrame(data)
print(df)

print("열 선택-------------")
print(df['Name'])
print(type(df['Name']))     # pandas.Series
print(df['Age'])

print("조건 필터링-------------")
print(df['Age'] > 30)
print(type(df['Age'] > 30))       # pandas.Series

print(df[df['Age'] > 30])
print(type(df[df['Age']>30]))     # pandas.DataFrame

# 데이터프레임 대괄호 안에
# 불리언 시리즈를 넣으면
# True인 행만 선택됨.

print("데이터 정렬-------------")
# 오름차순/ 내림차순
# sorted_df = df.sort_values(by='Age')    # 오름차순
sorted_df = df.sort_values(by='Age', ascending=False)   # 내림차순
print(sorted_df)

print("데이터 추가 및 삭제-------------")
# 열 추가
df['Salary'] = [5000, 6000, 7000]
print(df)

print("행 추가-------------")
# df.loc[3] = [4, 'David', 40, 8000]
df.loc[len(df)] = [4, 'David', 40, 8000]
print(df)

print("행 삭제-------------")
df = df.drop(1)
print(df)
# 행 번호 주의 ; 삭제된 채로 인덱스 번호는 그대로
# print(len(df))      # 3
# df.loc[len(df)] = [5, 'Eva', 50, 9000]  # 덮어쓰게 됨.
# print(df)

print("------------------")
# index 재정렬
# df1 = df.reset_index()  # 기존 인덱스를 새로운 열로 남겨준다.
# df1 = df.reset_index(drop=True)     # 기존 인덱스 정보 버리고, 새로 재정렬
# print(df1)

print("새 데이터프레임 생성-----")
data2 = {
    'ID' : [5, 6],
    'Name' : ['Eve', 'Frank'],
    'Age' : [28, 33]
}
df2 = pd.DataFrame(data2)
print(df2)

print("데이터 연결--------------")
# concated = pd.concat([df, df2])     # 중복된 인덱스 존재할 수 있음
concated = pd.concat([df, df2], ignore_index=True)  # 기존 인덱스 무시하고 새로운 인덱스로
print(concated)

print("데이터 병합--------------")
# 병합 시 기준열 필요
data3 = {
    'ID' : [1, 2, 3, 4, 5, 6],
    'Department' : ['HR',
                    'Engineering',
                    'Sales',
                    'R&D',
                    'Finance',
                    'Sales']
}
df3 = pd.DataFrame(data3)
print(df3)
print("------------------")
merged = pd.merge(concated, df3)    # 'ID'를 기준열로 해서 병합
print(merged)

print("결측치 처리--------------")
print(merged.isnull())  # True, False로 나온다.
print(merged.isnull().sum())  # null 개수의 합계(열 마다 기준)

# 결측치 채우기
meanVal = merged['Salary'].mean()   # 평균값 구하기
print(meanVal)
merged['Salary'] = merged['Salary'].fillna(meanVal)     # 결측값 채우기
print(merged)

print("------------------")
print(merged['Salary'].count())         # 개수
print(merged['Salary'].std())           # 표준편차
print(merged['Salary'].min())           # 최솟값
print(merged['Salary'].max())           # 최댓값
print(merged['Salary'].quantile(0.25))  # 4분위 지정값(25%)
print(merged['Salary'].quantile(0.5))   # 4분위 지정값(25%)
print(merged['Salary'].quantile(0.75))  # 4분위 지정값(25%)

# 특정 위치값 수정
# merged.loc[4, 'Salary'] = 8500
# print(merged)

print("중복 데이터 처리--------------")
data1 = {
    'ID' : [1, 3],
    'Name' : ['Alice', 'Charlie'],
    'Age' : [30, 25],
    'Salary' : [5000, 7000],
    'Department' : ['HR', 'Sales']
}
df1 = pd.DataFrame(data1)
df1 = pd.concat([merged, df1])
print(df1)
# 중복 확인
print(df1.duplicated())     # type: pandas.Series
print("--------------------")
# 중복 제거
df1_1 = df1.drop_duplicates()
print(df1_1)

