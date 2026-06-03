# hw08_1.py

# 3번
# 리스트 arr = [3, 6, 9, 12]가 주어졌을 때
# 첫 번째와 세 번째 요소를 스왑한 결과를 출력하는 코드를 작성하세요.

arr = [3, 6, 9, 12]
temp = arr[0]
arr[0] = arr[2]
arr[2] = temp
print(arr)
arr[0], arr[2] = arr[2], arr[0]
print(arr)

print("---------------------")
# 6. 리스트에서 첫 번째 짝수와 마지막 홀수를 찾아 서로 스왑하는 프로그램을 작성하시오.
a = [3, 6, 7, 4, 9, 10, 13]

# 첫 번째 짝수 인덱스 찾기
for i in range(0, len(a), 1):
    if a[i] % 2 == 0:
        break

# 마지막 홀수 인덱스 찾기
for j in range(len(a)-1, 0, -1):
    if a[j] % 2 == 1:
        break

temp = a[i]
a[i] = a[j]
a[j] = temp

print(a)

print("---------------------")

# 7. 파이썬으로 최대값을 찾는 알고리즘을 구현하시오.
def fmax(fa):
    max = fa[0]
    for sfa in fa:
        if max < sfa:
            max = sfa
    return max

print(fmax(a))

print("---------------------")
# 10. 주어진 딕셔너리에서 모든 값의 합을 구하는 함수를 작성하세요. 
# ( 예를 들어, 딕셔너리 { 'a': 10, 'b': 20, 'c': 30 }가 주어졌을 때, 합은 60 )

ca = { 'a': 10, 'b': 20, 'c': 30 }

def tot_dict(fa):
    value = 0
    for sfa in fa:
        value += fa[sfa]
    return value

print(tot_dict(ca))