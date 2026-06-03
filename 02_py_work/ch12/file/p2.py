# p2.py

path = r'ch12\file\계좌1.txt'
mode = 'r'  # 읽기 모드
encording = 'utf-8'

f = open(path, mode, encoding=encording)
lines = f.readlines()   # 리스트

accountList = []
# 반복문으로 각 라인 확인
for line in lines:
    # 1. 음수 슬라이싱(문자열 일부 내용 가져오기)
    # accountList.append(line[-14:-1])
    # accountList.append(line[-14:-1].strip()) 
    
    # 2. split() 함수 활용
    lineList = line.split()
    accountList.append(lineList[1])
# .strip() 앞, 뒤 공백 제거 메서드

print(accountList)

f.close()