try:
  print(x)
except NameError:
  print("Variable x is not defined") #
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished") #

try:
  x = int(input("Input an integer: "))
except(ValueError):
  print("It is not an integer.")

# files
try:
  f = open("file.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") #

x = 1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = 1
if not type(x) is int:
  raise TypeError("Only integers are allowed")
