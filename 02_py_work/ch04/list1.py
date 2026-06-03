# list1.py

# 변수명 = 데이터값

candy0 = "딸기맛"
candy1 = "레몬맛"
candy2 = "수박맛"
candy3 = "박하맛"
candy4 = "우유맛"
print(candy0)

candies = ["딸기맛", "레몬맛", "수박맛", "박하맛", "우유맛"]
print(candies)

print(candies[0])
print(candies[1])
print(candies[2])
print(candies[3])
print(candies[4])

# print(candies[5])

print("----------------------")
lista = ['list', 1, 0.7, True, [1, 2]]
print(lista)
print(type(lista))  # list

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

print(type(lista[0]))   # str
print(type(lista[1]))   # int
print(type(lista[2]))   # float
print(type(lista[3]))   # bool
print(type(lista[4]))   # list
print(lista[4][0])
print(lista[4][1])

print("----------------------")

ca = [10, 11, 21]
print(ca)
print(id(ca))
print(ca[0])
print(id(ca[0]))
print(ca[1])
print(id(ca[1]))
print(ca[2])
print(id(ca[2]))

print("----------------------")
# 값 변경하기
# 리스트변수명[인덱스] = 데이터값
a = [1, 2, 3, 4, 5]
a[2] = 30
print(a)
a[3] = 40
print(a)