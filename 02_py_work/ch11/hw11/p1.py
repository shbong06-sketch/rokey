# p1.py

# p.22 라디오버튼 구현 예제

from tkinter import Tk
from tkinter import Radiobutton
from tkinter import Label
from tkinter import Button
from tkinter import IntVar
from tkinter import messagebox

# 1. 위젯 생성
oroot = Tk()
oroot.title("Radio Button Practice")
oroot.geometry("400x300")

# 2. 라디오 버튼으로 어떤 메뉴를 선택했는지 저장하는 변수(1~4)
radio_value1 = IntVar()
radio_value1.set(-1)
radio_value2 = IntVar()
radio_value2.set(-1)

lunch = {0:"불고기 버거", 1:"치즈 버거", 2: "새우 버거", 3: "데리 버거"}
drink = {0:"코카 콜라", 1: "펩시 콜라", 2: "사이다", 3: "스프라이트"}

olabel1 = Label(oroot, text="버거를 고르세요.", bg="orange", pady=10)
olabel1.pack()
for i in range(len(lunch)):
    orad1 = Radiobutton(oroot, text=lunch[i], variable=radio_value1, value=i)
    orad1.pack()

olabel2 = Label(oroot, text="음료를 고르세요.", bg="blue", fg="white", pady=10)
olabel2.pack()
for i in range(len(drink)):
    orad2 = Radiobutton(oroot, text=drink[i], variable=radio_value2, value=i)
    orad2.pack()

# 기능: 선택된 라디오버튼 값을 변수로 가져와 메시지 박스에 출력
def order():
    val1 = radio_value1.get()
    val2 = radio_value2.get()
    response = messagebox.askokcancel("알림", lunch[val1]+", "+drink[val2]+"\n다음 메뉴를 주문하시겠습니까?")
    if response == 1:
        print(lunch[val1]+", "+drink[val2]+"\n다음 메뉴가 주문되었습니다.")
    else :
        print("주문이 취소되었습니다.")

obtn = Button(oroot, text="주문", padx=5, pady=5, command=order)
obtn.pack()

oroot.mainloop()