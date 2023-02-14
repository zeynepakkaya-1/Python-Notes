# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

def my_function(child3, child2, child1):
  print("The last child is " + child3)
my_function(child1 = "child1", child2 = "child2", child3 = "child3")

# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name
# tuple of arguments

def my_args(*kids):
  print("The first child is " + kids[0])
my_args("FirstChild", "SecondChild", "ThirdChild")

# Arbitrary Keyword Arguments, **kwargs
# dictionary of arguments

def my_kwargs(**kid):
  print("Kid's last name is " + kid["lname"])
my_kwargs(fname = "FirstName", lname = "LastName")

# default value
def my_function(country = "Turkey"):
  print("I am from " + country)
my_function() # I am from Turkey

# lambda
sum3 = lambda a, b, c : a + b + c
print(sum3(5, 10, 15)) # 30

def myMultiplier(n):
  return lambda a : a * n

mydoubler = myMultiplier(2)
mytripler = myMultiplier(3)

print(mydoubler(11)) # 22
print(mytripler(11)) # 33