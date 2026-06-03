# pack.py

from tkinter import Tk
from tkinter import Button

# 1. 위젯 생성
otk = Tk()
otk.geometry('300x200')

obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")

# 2. 위젯 배치
obtn1.pack(side='left')     # side 디폴트 값: "top"
obtn2.pack(side='right')
obtn3.pack(side='bottom')

otk.mainloop()
