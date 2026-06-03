# grid.py

from tkinter import Tk
from tkinter import Button

# 1. 위젯 생성
otk = Tk()
otk.geometry('300x200')

obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")
obtn4 = Button(otk, text = "PUSH4")


# 2. 위젯 배치
# grid: 상대적인 순서를 고려하여 배치
obtn1.grid(row= 1, column= 0)
obtn2.grid(row= 1, column= 1)
obtn3.grid(row= 0, column= 4)
obtn4.grid(row= 2, column= 3, padx=10, pady=20)     # 여백을 통해 추가적인 배치 가능

otk.mainloop()
