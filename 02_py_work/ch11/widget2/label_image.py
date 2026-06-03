# label_image.py

from tkinter import Tk
from tkinter import Button
from tkinter import PhotoImage
from tkinter import Label

# 1. 위젯 생성
otk = Tk()
otk.geometry('400x300')

# PNG 파일 형식 활용 가능
# img1 = PhotoImage(file='C:/rokey/py_work/ch11/widget2/apple.png') # 절대경로 ; 경로 복사 => 슬래쉬 방향 변경 '/'
img1 = PhotoImage(file='./ch11/widget2/apple.png')                  # 상대경로

img_label = Label(otk, image=img1)
img_label.place(x=-20, y=-20)

obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")

obtn1.place(x=10, y=60)
obtn2.place(x=140, y=60)
obtn3.place(x=80, y=10)

otk.mainloop()
