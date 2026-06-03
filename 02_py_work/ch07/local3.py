# local3.py
# def scope_test() :
#     a = a + 3       # 전역변수(재할당)
#     print("scope_test() 함수 안의 a 값은", a)

# a = 0   # 전역변수 선언(초기화)
# print("scope_test() 함수 밖의 a 값은", a)
# scope_test()
# print("scope_test() 함수 호출 후 a 값은", a)

print("-----------------------------------")
# 1. scope_test() 함수 내 a 변수 값을 전역 변수 선언
def scope_test() :
    global a        # 가급적 함수 내 첫번째 줄에서 선언할 것(읽기 어려워)
    a = a + 3       # 전역변수(재할당)
    print("scope_test() 함수 안의 a 값은", a)

a = 0   # 전역변수 선언(초기화)
print("scope_test() 함수 밖의 a 값은", a)
scope_test()
print("scope_test() 함수 호출 후 a 값은", a)


print("-----------------------------------")
# 2. scope_test() 함수 내 a 변수 값을 지역 변수로 초기화
def scope_test() :
    a = 0
    a = a + 3
    print("scope_test() 함수 안의 a 값은", a)
    return a

a = 0   # 전역변수 선언(초기화)
print("scope_test() 함수 밖의 a 값은", a)
a = scope_test()
print("scope_test() 함수 호출 후 a 값은", a)
