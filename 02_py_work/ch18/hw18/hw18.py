# hw18.py

# 6.
import pandas as pd
path = r'ch18\hw18\data.csv'
df = pd.read_csv(path)

print(f'Age 평균: {df['Age'].mean()}, 최댓값: {df['Age'].max()}, 최솟값: {df['Age'].min()}')
print(f'Salary 평균: {df['Salary'].mean()}, 최댓값: {df['Salary'].max()}, 최솟값: {df['Salary'].min()}')

print("--------------------------")
# 7.
# filtered = df[df['Age'] >= 30]
# filtered = filtered[filtered['Salary'] >= 60000]
filtered = df[(df['Age'] >= 30) & (df['Salary'] >= 60000)]
print(filtered)

print("--------------------------")
# 8.
import numpy as np
origin = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
squared = origin**2
print('원본 배열:', origin)
print('제곱 배열:', squared)
print(f'평균: {squared.mean()}, 최댓값: {squared.max()}, 최솟값: {squared.min()}')

print("--------------------------")
# 9.
import numpy as np
arr = np.random.randint(1, 12, (3, 4))
max_arr = np.array([arr[0, :].max(), arr[1, :].max(), arr[2, :].max()])
print('원본 행렬:\n', arr)
print('각 행의 최댓값:', max_arr)

print("--------------------------")
# 10.
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("title")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.grid()
plt.show()