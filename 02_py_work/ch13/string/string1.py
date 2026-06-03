# string1.py

muna = 'python'
print(muna[0])
print(muna[1])
print(muna[2])
print(type(muna))

try:
    muna[0] = 'k'   # TypeError ; 문자열의 개별 인덱스에는 값 할당 불가
except TypeError as e:
    print(type(e), e)

munb = ['python']
print(munb[0])
print(type(munb))

munc = ['p', 'y', 't', 'h', 'o', 'n']
print(munc[0])
print(munc[1])
print(munc[2])
print(type(munc))
munc[0] = 'k'
print(munc)

print("------------------------")
for i in range(0,6,1):
    print(munc[i], end='')
print()

length = len(munc)
print(length)
for i in range(0, len(munc), 1):
    print(munc[i], end='')
print()

print("------------------------")
print(ord("A"))     # 인코딩
print(ord("a"))

print(chr(65))      # 디코딩
print(chr(97))

print(ord('가'))    # 유니코드 인코딩
print(chr(44032))   # 유니코드 디코딩

print("------------------------")
ma = 'ChatGPT'+'를 활용한 python'
print(ma)
print(type(ma))

print("------------------------")
### 다양한 문자열 사용(출력) 방법
# 표준 출력 함수: print(인수) 활용
# 1. 기능: 인수를 모니터 출력
# 2. 인수: 객체(다양한 자료형 모두)
# 3. 반환: 없음(None)

name = '홍길동'
age = 510
# 기본 형식
print("이름:", name, "나이:", age)

# 1. % 연산자 사용 방식
# 서식문자 활용 => %s: 문자열, %d: 10진수, %f: 실수형, %x: 16진수 ...
print("이름: %s 나이: %d"%(name, age))

# 2. format() 메서드 사용 방식
print("이름: {} 나이: {}".format(name, age))

# 3. f-string 사용 방식
print(f"이름: {name} 나이: {age}")

# 소수점 자리수 맞추기
pi = 3.141592
print(f"파이: {pi}")
print("파이: %.2f"%pi)
print("파이: {:.2f}".format(pi))
print(f"파이: {pi:.2f}")        # f"{값: 포멧옵션}""

print("------------------------")
# 슬라이싱
# 변수명[시작인덱스: 끝인덱스: 스텝]
muna = 'python'
print(muna[0:6])
print(muna[:])
print(muna[0:])
print(muna[:6])
print(muna[-3:])    # hon
print(muna[2:-2])   # th