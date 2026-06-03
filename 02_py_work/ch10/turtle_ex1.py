# turtle_ex1.py

# 라이브러리를 import 해서 사용할 수 있다
import turtle

turtle.shape('turtle')

# 거북이를 100걸음 전진
# turtle.forward(100)

# 거북이의 방향을 120도 왼쪽으로
# turtle.left(120)

for x in range(1, 100, 1): # 1 ~ 99
    turtle.forward(x)
    turtle.left(90)


from turtle import *
from turtle import Turtle
from turtle import shape

shape('turtle')

for x in range(1, 100, 1): # 1 ~ 99
    forward(x)
    left(90)
