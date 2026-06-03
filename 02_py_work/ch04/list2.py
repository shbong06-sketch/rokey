# list2.py

# list 값 추가하기
# 리스트명.append(추가할 값)

listc = []          # 빈 리스트
print(listc)
print(type(listc))  # list

listc.append(300)
print(listc)
listc.append("Python")
print(listc)
listc.append(3.14)
print(listc)
listc.append(False)
print(listc)
listc.append([1, True])
print(listc)

print("---------------------")
# list 값 제거하기
# 리스트명.remove(제거할 값)

subject = ["국어", "수학", "영어", "국사"]
print(subject)

subject.append("영어")
print(subject)

subject.remove("영어")
print(subject)

print("---------------------")
clovers = ['클로버1', '클로버2', '클로버3']
print(clovers[1])
print(clovers)
del clovers[1]
print(clovers)

print(clovers[1])
del clovers[1]
print(clovers)

print("---------------------")
# 특정 위치에 값 추가하기
clovers = ['클로버1', '클로버2', '클로버3']
print(clovers)
clovers.insert(1, "클로버4")
print(clovers)
# 클로버5를 리스트의 맨 앞에 추가하세요.
clovers.insert(0, '클로버5')
print(clovers)
print(clovers[0])
print(clovers[4])

clovers.insert(6, '클로버6')
clovers.append('클로버7')
print(clovers)
print(clovers[5])

print("---------------------")
# 여러 값 추가
clovers.extend(['클로버8', '클로버9'])
print(clovers)
