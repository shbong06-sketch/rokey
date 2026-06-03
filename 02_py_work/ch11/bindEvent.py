# bindEvent.py

from tkinter import Tk
from tkinter import Button
from tkinter import Label

# 1. 위젯 생성
otk = Tk()
otk.geometry('300x200')

def order():
    print("주문합니다.")

olabel1 = Label(otk, text = '치즈버거 (5000원)')
olabel2 = Label(otk, text = '불고기버거 (5000원)')
olabel3 = Label(otk, text = '새우버거 (6500원)')
obtn = Button(otk, text = "주문" , command = order)

# 2. 위젯 배치
olabel1.pack()
olabel2.pack()
olabel3.pack()
obtn.pack()

otk.mainloop()  # 주요 반복구조 동작하며 부모 위젯 실행