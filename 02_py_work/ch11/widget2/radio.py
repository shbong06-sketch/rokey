# radio.py

from tkinter import Tk
from tkinter import Button
from tkinter import Radiobutton
from tkinter import IntVar

# 1. 위젯 생성
otk = Tk()
otk.geometry('300x200')

# 어떤 메뉴를 선택했는지 저장하는 변수
radio_value = IntVar()      # 정수형 변수 저장 객체 생성 ; tkinter에서는 클래스 객체를 만들어 변수 저장
radio_value.set(-1)         # 기본값으로 아무것도 선택 안하도록 설정하는 방법
# radio_value.set(2)        # 정수값 설정
# val = radio_value.get()   # (설정/저장된)정수값 접근
# print(val)
lunch = {0: 'A런치', 1: 'B런치', 2: 'C런치', 5: 'D런치'}

# radio_value => 어떤 버튼이 선택되어 있는지 저장할 변수
# variable => 클릭된 버튼의 정보를 저장할 변수명 설정
# value => radio_value에 저장될 데이터를 지정하는 인수
orad1 = Radiobutton(otk, text=lunch[0], variable=radio_value, value=0)
orad2 = Radiobutton(otk, text=lunch[1], variable=radio_value, value=1)
orad3 = Radiobutton(otk, text=lunch[2], variable=radio_value, value=2)
orad4 = Radiobutton(otk, text=lunch[5], variable=radio_value, value=5)

# 기능: 선택된 라디오버튼의 값을 변수로 가져와 출력
def buy():
    print("다음 메뉴를 주문합니다:", end =" ")
    val = radio_value.get()     # 정수값 접근
    print(lunch[val])

obtn1 = Button(otk, text = "주문" , command = buy)

# 2. 위젯 배치
orad1.pack()
orad2.pack()
orad3.pack()
orad4.pack()
obtn1.pack()

otk.mainloop()


# class InvVar:
#     def __init__(self):
#         self.int_val = 0

#     def set(self, int_val):
#         self.int_val = int_val

#     def get(self):
#         return self.int_val