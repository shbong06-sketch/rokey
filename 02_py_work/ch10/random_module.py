# random_module.py

import random

animals = ['체셔고양이', '오리', '도도새', '호랑이', '고래']
print(random.choice(animals))
print(random.choice(animals))
print(random.choice(animals))

print("-----------------------")
print(random.sample(animals, 2))
print(random.sample(animals, 3))

print("-----------------------")
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))
