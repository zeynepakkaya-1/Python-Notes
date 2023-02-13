# Tuple items are ordered, unchangeable, and allow duplicate values.

car_brands = ("Dodge", "Ram Trucks", "GMC")

print(len(car_brands)) # 3

one_item_tuple = ("one",)
print(type(one_item_tuple)) # <class 'tuple'>

# tuple constructor
print(tuple(("Dodge", "Ram Trucks", "GMC"))) # ('Dodge', 'Ram Trucks', 'GMC')

add_to_car_brands = ("Nissan",)
car_brands += add_to_car_brands
print(car_brands) # ('Dodge', 'Ram Trucks', 'GMC', 'Nissan')

# del keyword
del one_item_tuple
del add_to_car_brands

# Unpacking a tuple:
(car_brand1, car_brand2, car_brand3, car_brand4) = car_brands
print(car_brand1)
print(car_brand2)
print(car_brand3)
print(car_brand4)

(car_brand1, *car_brand2_3_4) = car_brands
print(car_brand1)
print(car_brand2_3_4) # ['Ram Trucks', 'GMC', 'Nissan']

(car_brand1, *car_brand2_3, car_brand4) = car_brands
print(car_brand1)
print(car_brand2_3) # ['Ram Trucks', 'GMC']
print(car_brand4)

print(car_brands * 2) # ('Dodge', 'Ram Trucks', 'GMC', 'Nissan', 'Dodge', 'Ram Trucks', 'GMC', 'Nissan')

# .count()
print((car_brands * 2).count("Dodge")) # 2

# index()
print((car_brands * 2).index("Dodge")) # 0
