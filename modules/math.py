# min max abs pow

print(min(5, 10, 25)) # 5
print(max(5, 10, 25)) # 25

print(abs(-7.25)) # 7.25

print(pow(4, 3)) # 64
print(pow(3, 4)) # 81

print(round(3.5)) # 4
print(round(4.5)) # 4

print(bin(3)) # 0b11
print(bin(2)) # 0b10
print(bin(1)) # 0b1

import math

# sqrt ceil floor

print(math.sqrt(64)) # 8.0
print(math.sqrt(81)) # 9.0

print(math.ceil(1.1)) # 2
print(math.floor(1.9)) # 1

# pi e inf nan
print(math.pi) # 3.141592653589793
print(math.e) # 2.718281828459045
print(math.inf)
print(math.nan)

# log log10 log2
print(math.log(math.e)) # 1.0
print(math.log10(100)) # 2.0
print(math.log2(4)) # 2.0

# radians degrees
print(math.radians(180)) # 3.141592653589793
print(math.radians(90)) # 1.5707963267948966
print(math.radians(45)) # 0.7853981633974483

# cos sin tan
print(math.cos(3.141592653589793)) # -1.0
print(math.sin(1.5707963267948966)) # 1.0
print(math.tan(0.7853981633974483)) # 0.9999999999999999

# acos asin atan
print(math.acos(-1.0)) # 3.141592653589793
print(math.asin(1.0)) # 1.5707963267948966
print(math.atan(0.9999999999999999)) # 0.7853981633974483

# factorial
print(math.factorial(5)) # 120

# isinf isfinite isnan
print(math.isinf(math.inf)) # True
print(math.isfinite(math.inf)) # False
print(math.isnan(math.nan)) # True
