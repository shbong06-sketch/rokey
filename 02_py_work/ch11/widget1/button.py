# button.py
# from tkinter import *
from tkinter import Tk
from tkinter import Button

# 1. 위젯 생성
otk = Tk()      # 부모 윈도우 위젯 객체 생성
# 배치 원점은 좌상단
otk.geometry('100x150+400+400')     # 단위(픽셀, px)
# otk.geometry('100x150')     # 단위(픽셀, px)

def hello1():
    print("버튼 1번이 눌렸음")
def hello2():
    print("버튼 2번이 눌렸음")
def hello3():
    print("버튼 3번이 눌렸음")

def hello(btn):
    print("버튼", btn, "번이 눌렸음")

obtn1 = Button(otk, text = "PUSH1" , command = hello1)     # 자식 위젯 객체 생성 ; 부모 인스턴스와 위젯 클래스 객체 연결
obtn2 = Button(otk, text = "PUSH2" , command = hello2)
obtn3 = Button(otk, text = "PUSH3" , command = hello3)

# obtn1 = Button(otk, text = "PUSH1" , command = lambda : hello(1))
# obtn2 = Button(otk, text = "PUSH2" , command = lambda : hello(2))
# obtn3 = Button(otk, text = "PUSH3" , command = lambda : hello(3))

# 2. 위젯 배치
obtn1.pack()     # 위젯 배치
obtn2.pack()
obtn3.pack()

# 3, 이벤트 및 바인딩
# 푸쉬/누름(버튼 이벤트) 발생 시, 특정 동작이 수행(바인딩)

otk.mainloop()  # 주요 반복구조 동작하며 부모 위젯 실행