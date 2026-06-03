# optimize.py

from scipy.optimize import minimize
# convex 함수의 최솟값 구할 때 주로 사용
def f(x):
    return x**2 + 4 * x + 4

result = minimize(f, x0=0)
print(f"Optimal value: {result.x}")

# minimize는 주어진 시작점에서 함수값을 줄여가는 알고리즘
# Convex 함수(아래로 볼록한 함수)가 아니어도 실행은 되나
# 결과가 원하는 값이 아닐 수 있음

# Convex 함수 특징
#   - 아래로 볼록
#   - local minimum = global minimum

def f1(x):
    return x**4 + 3*x**2

result = minimize(f1, x0=0)
print(f"Optimal value: {result.x}")
# 초기값에 따라 다른 결과 도출
# x0= -2 => 왼쪽 최소값
# x0= 2 => 오른쪽 최소값