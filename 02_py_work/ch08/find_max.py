# find_max.py

# 최댓값 찾기
print("1--------------------")
ca = [10, 17, 13, 11]
max = ca[0]
if max < ca[1]:
    max = ca[1]
if max < ca[2]:
    max = ca[2]
if max < ca[3]:
    max = ca[3]
print(max)

print("2--------------------")
ca = [10, 17, 13, 11]
max = ca[0]
for sb in range(1, 4, 1):
    if max < ca[sb]:
        max = ca[sb]
print(max)

print("3--------------------")
ca = [10, 17, 13, 11]
max = ca[0]
for sb in ca:
    if max < sb:
        max = sb
print(max)