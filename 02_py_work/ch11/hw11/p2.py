# p2.py
# p.28 체크박스 예제

from tkinter import Tk
from tkinter import Button
from tkinter import Checkbutton
from tkinter import BooleanVar
from tkinter import messagebox

# 1. 위젯 생성
oroot = Tk()
oroot.title("CheckBox Practice")
oroot.geometry("400x300")

coffee = {0:"아메리카노", 1:"라떼", 2:"카푸치노", 3:"에스프레소"}
check_value = {}

for i in range(len(coffee)):
    check_value[i] = BooleanVar()
    ocheckbutton = Checkbutton(oroot, text=coffee[i],variable=check_value[i])
    ocheckbutton.pack(anchor="w")

# 기능: 선택된 체크버튼의 값을 변수로 가져와 메시지 박스로 출력
def order():
    order_list = []
    for i in range(len(coffee)):
        if check_value[i].get():
            order_list.append(coffee[i])
    response = messagebox.askokcancel("주문확인", ', '.join(order_list)+"\n다음 메뉴를 주문하시겠습니까?")
    if response == 1:
        print(', '.join(order_list)+"\n다음 메뉴 주문이 완료되었습니다.")
    else :
        print("주문이 취소되었습니다.")
 
obtn = Button(oroot, text="주문하기", command=order)
obtn.pack()            

oroot.mainloop()