# find_root.py
from scipy.optimize import root

def equation(x):
    return x**2 - 4

sol = root(equation, x0=1)
print(f"root: {sol.x}")

# '함수값이 0이 되는 x를 찾는다'는 전제를 가지고 작동