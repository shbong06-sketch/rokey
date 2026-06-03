# label_image1.py

from tkinter import Tk
from tkinter import Button
from tkinter import PhotoImage
from tkinter import Label

# 이미지 변환 : 외장 라이브러리 활용
# - 라이브러리 다운로드 수행 후 설치
# - PIL(pillow) 라이브러리
# - 터미널에 아래 명령어 입력
# - 설치 확인: pip list > 설치된 라이브러리 확인 가능
# - 설치 명령: pip install pillow(라이브러리명)
from PIL import Image
image = Image.open('C:/rokey/py_work/ch11/widget2/apple1.jpg')
image.save('C:/rokey/py_work/ch11/widget2/apple1.png', format="PNG")
print("이미지가 PNG로 변환되었습니다.")

# 1. 위젯 생성
otk = Tk()
otk.geometry('400x300')

# PNG 파일 형식 활용 가능
img1 = PhotoImage(file='C:/rokey/py_work/ch11/widget2/apple1.png') # 경로 복사 => 슬래쉬 방향 변경 '/'

img_label = Label(otk, image=img1)
img_label.place(x=-20, y=-20)

obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")

obtn1.place(x=10, y=60)
obtn2.place(x=140, y=60)
obtn3.place(x=80, y=10)

otk.mainloop()
