hello_str = "Hello"
print(hello_str[0]) # H

for letter in "Hello":
    print(letter)

# len() function = length
print(len("Hello")) # 5

# in keyword
print("H" in "Hello") # True
# not in keyword
print("H" not in "Hello") # False

# Slicing
print("Hello World"[2:5]) # llo
print("Hello World"[:5]) # Hello
print("Hello World"[2:]) # llo World
print("Hello World"[-5:-2]) # Wor

# .upper()
print("zeynep".upper())
# .lower()
print("ZEYNEP".lower())
# .isupper()
print("zeynep".upper().isupper()) # True
# .islower()
print("ZEYNEP".lower().islower()) # True
# .casefold()
print("ZEYNEP".casefold()) # zeynep
# .casefold() method converts more characters into lower case than .lower()

# .swapcase()
print("ZeYNeP".swapcase()) # zEynEp

# .capitalize()
print("zeyNEP akkaya".capitalize()) # Zeynep akkaya
# .title()
print("zeyNEP akkaya".title()) # Zeynep Akkaya
# .istitle()
print("zeyNEP akkaya".title().istitle()) # True

# .strip()
print("   Hi   ".strip()) #-Hi-
# .lstrip()
print("   Hi   ".lstrip()) #-Hi   -
# .rstrip()
print("   Hi   ".rstrip()) #-   Hi-

# .replace()
print("Hello".replace("H", "X")) # Xello

# .startswith()
print("Hello".startswith("H")) # True
# .endswith()
print("Hello".endswith("o")) # True

# .split()
print("Hi.Hello.Welcome".split(".")) # ['Hi', 'Hello', 'Welcome']

# .format()
my_name = "Zeynep"
my_age = 21
print("My name is {}, and I am {}".format(my_name, my_age)) # My name is Zeynep, and I am 21
print("My name is {0}, and I am {1}".format(my_name, my_age)) # My name is Zeynep, and I am 21

# \ escape character
print("I love \"Vikings\".") # I love "Vikings".

print("I love\nVikings.") # new-line
print("I love\tVikings.") # tab
print("I love\rVikings.") # carriage return
print("I love \bVikings.") # back space # I loveVikings.
