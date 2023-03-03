def print_func():
    print("Hi")


def decorator_func(func):
    def wrapper_func():
        print(f"The name of the function is {func.__name__}")
        return func()
    return wrapper_func


decorator = decorator_func(print_func)
decorator()
"""
The name of the function is print_func
Hi
"""


@decorator_func
def print_func(): print("Hi")


print_func()
"""
The name of the function is print_func
Hi
"""


# with arguments
def name_func(name, age):
    print(f"Name: {name}, Age {age}")


def decorator_func(func):
    def wrapper_func(*args):
        print(f"The name of the function is {func.__name__}")
        return func(*args)
    return wrapper_func


decorator = decorator_func(name_func)
decorator("Zeynep", 21)
"""
The name of the function is name_func
Name: Zeynep, Age 21
"""


@decorator_func
def func(name, age):
    print(f"Name: {name}, Age {age}")


func("Zeynep", 21)
"""
The name of the function is func
Name: Zeynep, Age 21
"""