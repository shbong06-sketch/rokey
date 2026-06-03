# tkinter_module.py

import tkinter          # 라이브러리 모듈 불러오기

# 1. 위젯 생성
otk = tkinter.Tk()      # 부모 윈도우 위젯 객체 생성

def hello():
    print("Hello!")

obtn = tkinter.Button(otk, text = "click" , command = hello)     # 자식 위젯 객체 생성 ; 부모 인스턴스와 위젯 클래스 객체 연결

# 2. 위젯 배치
obtn.pack()     # 위젯 배치

# 3, 이벤트 및 바인딩
# 푸쉬/누름(버튼 이벤트) 발생 시, 특정 동작이 수행(바인딩)

otk.mainloop()  # 주요 반복구조 동작하며 부모 위젯 실행