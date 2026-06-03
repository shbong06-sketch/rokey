# file_write.py
# 파일객체명.write(data)

# 참고: 현재 인코딩 방식 확인하는 방법
# import locale
# print(locale.getpreferredencoding())  # cp949

f = open(r'ch12\file1.txt', 'w')
# f = open(r'ch12\file1.txt', 'w', encoding='utf-8')

# f.write('hello')
# f.write('안녕!')
# 인코딩 수행(CP949) - 파이썬 기본 인코딩
# VS코드 기본 인코딩 UTF-8
# => 두 가지가 달라서 한글이 깨져서 나온다.
# => 인코딩과 디코딩 방식을 통일 시켜야 한다.
# (일반적으로 utf-8이 자주 사용)

for i in range(1, 11):  # 1~10 int
    data = "%d번째 줄입니다.\n" % i
    # % 형식지정자. 문자열에 형식을 지정해 데이터를 삽입할 때 사용
    f.write(data)
    
f.close()