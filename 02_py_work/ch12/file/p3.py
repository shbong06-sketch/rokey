# p3.py

path = r'ch12\file\계좌1.txt'
mode = 'r'

with open(path, mode, encoding='utf-8') as f:
    lines = f.readlines()
    account_Dict = {}
    for line in lines:
        lineList = line.split()
        account_Dict[lineList[0]] = lineList[1]

mode = 'a'
with open(path, mode, encoding='utf-8') as f:
    data1 = '강호동 147-12-002093\n'
    data2 = '유재석 146-22-102093\n'
    f.write(data1)
    f.write(data2)


print(account_Dict)