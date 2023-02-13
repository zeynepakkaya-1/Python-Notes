# List items are ordered, changeable, and allow duplicate values.

car_brands = ["Dodge", "Ram Trucks", "GMC"]

print(type(car_brands)) # <class 'list'>

# len() function
print(len(car_brands)) # 3

# list() constructor
print(list(("Dodge", "Ram Trucks", "GMC"))) # ['Dodge', 'Ram Trucks', 'GMC']

print(car_brands[2]) # GMC
print(car_brands[-1]) # GMC

# in keyword
print("GMC" in car_brands) # True

for i in car_brands:
    print(i)
for i in range(len(car_brands)):
    print(car_brands[i])
i = 0
while i < len(car_brands):
    print(car_brands[i])
    i += 1
[print(i) for i in car_brands] # ***

car_brands_include_a = []
for i in car_brands:
    if "a" in i:
        car_brands_include_a.append(i)
print(car_brands_include_a) # ['Ram Trucks']

# list comprehension
car_brands_include_a = [i for i in car_brands if "a" in i]
print(car_brands_include_a) # ['Ram Trucks']

# numbers 0 through 9:
print([x for x in range(10)]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([x**2 for x in range(4)]) # [0, 1, 4, 9]
print([x**2 if x**2 % 2 == 0 else "odd number" for x in range(4)]) # [0, 'odd number', 4, 'odd number']

# .insert()
car_brands.insert(1, "Nissan")
print(car_brands) # ['Dodge', 'Nissan', 'Ram Trucks', 'GMC']

# .append()
car_brands.append("Honda")
print(car_brands) # ['Dodge', 'Nissan', 'Ram Trucks', 'GMC', 'Honda']

# .extend()
car_brands.extend(["BMW", "Mercedes"])
print(car_brands) # ['Dodge', 'Nissan', 'Ram Trucks', 'GMC', 'Honda', 'BMW', 'Mercedes']

# .remove()
car_brands.remove("Honda")
print(car_brands) # ['Dodge', 'Nissan', 'Ram Trucks', 'GMC', 'BMW', 'Mercedes']

# .pop()
popped_car_brand = car_brands.pop()
print(popped_car_brand) # Mercedes
print(car_brands) # ['Dodge', 'Nissan', 'Ram Trucks', 'GMC', 'BMW']

popped_car_brand = car_brands.pop(1)
print(popped_car_brand) # Nissan
print(car_brands) # ['Dodge', 'Ram Trucks', 'GMC', 'BMW']

# .sort()
car_brands.sort()
print(car_brands) # ['BMW', 'Dodge', 'GMC', 'Ram Trucks']

car_brands.sort(reverse=True)
print(car_brands) # ['Ram Trucks', 'GMC', 'Dodge', 'BMW']

# del keyword
del car_brands[3]
print(car_brands) # ['Ram Trucks', 'GMC', 'Dodge']

# .reverse()
car_brands.reverse()
print(car_brands) # ['Dodge', 'GMC', 'Ram Trucks']

# .copy()
car_brands_copy = car_brands.copy()
# list()
car_brands_copy2 = list(car_brands)

print(car_brands_copy + car_brands_copy2) # ['Dodge', 'GMC', 'Ram Trucks', 'Dodge', 'GMC', 'Ram Trucks']

# .count()
print((car_brands_copy + car_brands_copy2).count("GMC")) # 2

# .index()
print((car_brands_copy + car_brands_copy2).index("GMC")) # 1

# .clear()
car_brands.clear()
print(car_brands) # []

del car_brands
del car_brands_copy
del car_brands_copy2
