# text.py


from tkinter import Tk
from tkinter import Text


# 1. 위젯 생성
root = Tk()
root.geometry("400x350")

txt = Text(root, width=30, height=10)
txt.pack()

root.mainloop()