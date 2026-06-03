# checkbutton1.py

from tkinter import Tk
from tkinter import Button
from tkinter import Checkbutton
from tkinter import BooleanVar

# 1. 위젯 생성
otk = Tk()
otk.geometry('300x200')

coffee = {0: '아메리카노', 1: '라떼', 2: '카푸치노', 3: '에스프레소'}
check_value = {}        # 빈 딕셔너리 생성
# 불리언 변수 4개 생성
for i in range(len(coffee)):
    check_value[i] = BooleanVar()
# print("check_value: ", check_value)

for i in range(len(coffee)):
    ocheckbutton = Checkbutton(otk, text=coffee[i], variable=check_value[i])
    ocheckbutton.pack()     # 2. 위젯 배치

# 기능: 선택된 체크버튼의 값을 변수로 가져와 출력
def buy():
    print("다음 메뉴를 주문합니다:")
    for i in range(len(coffee)):
        if check_value[i].get():
            print(coffee[i])

obtn1 = Button(otk, text = "주문" , command = buy)

# 2. 위젯 배치
obtn1.pack()

otk.mainloop()