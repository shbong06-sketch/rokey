# tuple1.py

clovers = ('클로버1', '하트2', '클로버3')
print(clovers[1])

print(clovers)
print(type(clovers))       # tuple

# clovers[1] = "클로버2"

print("--------------------")

my_tuple1 = ()             # 빈 튜플
print(my_tuple1)
print(type(my_tuple1))

my_tuple2 = (1, -2, 3.14, True, "hi", [1, 2])
print(my_tuple2)

my_tuple3 = 1, -2, 3.14, True, "hi", [1, 2]
print(my_tuple3)
print(type(my_tuple3))

# clovers[3] = False        # TypeError

print("--------------------")

my_int = (1)
print(type(my_int))         # int
my_int = (1, )
print(type(my_int))         # tuple
my_int = [1]
print(type(my_int))         # int

print("--------------------")
# 형 변환 : list(), tuple()
my_list3 = list(my_tuple3)
print(my_list3)
print(type(my_list3))
my_list3[3] = False
print(my_list3)

print("--------------------")

my_tuple3 = tuple(my_list3)
print(my_tuple3)
print(type(my_tuple3))

print("--------------------")
