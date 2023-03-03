print(*[1, 2, 3, 4]) # 1 2 3 4

print(*[1, 2, 3, 4], *[5, 6, 7, 8]) # 1 2 3 4 5 6 7 8

d1 = {"name": "Zeynep"}
d2 = {"age": 21}

print({**d1, **d2}) # {'name': 'Zeynep', 'age': 21}

print(*"hi") # h i