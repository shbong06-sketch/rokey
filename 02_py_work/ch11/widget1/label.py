# label.py

from tkinter import Tk
from tkinter import Label

# 1. 위젯 생성
otk = Tk()
otk.geometry("400x350")

olabel1 = Label(otk, text = '적', bg='red', width= 20)
olabel2 = Label(otk, text = '녹', bg='green', width= 20)
olabel3 = Label(otk, text= '파', bg='blue', width= 20)

# 2. 위젯 배치
olabel1.pack()
olabel2.pack()
olabel3.pack()

# 3. 이벤트 및 바인딩


otk.mainloop()
