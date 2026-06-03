# func_call.py

# 기능 / 동작 : 절대값 출력 함수

def myabs(arg) :
    if(arg < 0) :
        result = arg * -1
    else :
        result = arg
    return result

print(myabs(10))
print(myabs(-10))

print("-----------------------------------")
def funca() :
    print("a 함수 호출")

def funcb() :
    funca()                 # 세번째 호출
    print("b 함수 호출")    

def funcc() :
    funcb()                 # 두번째 호출
    print("c 함수 호출")

funcc()                     # 첫번째 호출