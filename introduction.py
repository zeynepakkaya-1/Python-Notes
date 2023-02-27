# Python can be used on a server to create web applications.
# It was created by Guido van Rossum, and released in 1991.

"""
multi-line
comment
"""

'''
multi-line
comment
'''

# Variables can change type after they have been set.
first_int_then_str = 5
first_int_then_str = "W3Schools"

# Casting:
str3 = str(3) # '3'
int3 = int(3) # 3
float3 = float(3) # 3.0

# type() function:
print(type(str3))
print(type(int3))
print(type(float3))

car_brand1, car_brand2, car_brand3 = "Dodge", "Ram Trucks", "GMC"
print(car_brand1)
print(car_brand2)
print(car_brand3)

# Unpack a list:
car_brands = ["Dodge", "Ram Trucks", "GMC"]
car_brand1, car_brand2, car_brand3 = car_brands
print(car_brand1)
print(car_brand2)
print(car_brand3)

# Unpack a tuple:
car_brands = ("Dodge", "Ram Trucks", "GMC")
car_brand1, car_brand2, car_brand3 = car_brands
print(car_brand1)
print(car_brand2)
print(car_brand3)

best_classic_car1 = best_classic_car2 = best_classic_car3 = "1969 Chevrolet El Camino"
print(best_classic_car1)
print(best_classic_car2)
print(best_classic_car3)

print(car_brand1, car_brand2, car_brand3) # Dodge Ram Trucks GMC
print(car_brand1 + car_brand2 + car_brand3) # DodgeRam TrucksGMC

# print(5 + "str") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(5, "str") # 5 str

# global keyword:
# If you want to change a global variable's value inside a function
# If you want to declare a global variable inside a function instead of local variable

# Data Types:
# str, int, float, complex (1j) (j is imaginary part), list, tuple, range
# dict {"one": 1, "two": 2}
# set ({"one", "two"}), frozenset frozenset({"one", "two"})
# bool, bytes b"Hi", bytearray bytearray(5), memoryview memoryview(bytes(5))
# NoneType x = None

scientific_float1 = 45e3 # 45 x 10^3
scientific_float2 = 32E4 # 32 x 10^4

complex(1) # 1 + 0j

# Any string, list, tuple, set, and dictionary is True, except empty ones.
# Any number is True, except 0.

# isinstance() method
print(isinstance(200, int)) # True

print(20 / 6) # 3.3
print(20 // 6) # 3
