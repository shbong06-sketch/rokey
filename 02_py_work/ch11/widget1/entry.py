# entry.py

from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar

# 1. 위젯 생성
otk = Tk()
otk.geometry("400x350")

ostring = StringVar()
oentry = Entry(otk, textvariable= ostring)
olabel = Label(otk, textvariable= ostring, bg = 'coral', width = 20)


# 2. 위젯 배치
oentry.pack()
olabel.pack()

# 3. 이벤트 및 바인딩


otk.mainloop()
