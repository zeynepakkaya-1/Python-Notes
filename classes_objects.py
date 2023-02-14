# __init__() function, __str__() function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"
  
  def greeting(self):
    print("Hi, my name is " + self.name + ".")

person1 = Person("Zeynep", 21)

print(person1) # Zeynep(21)
print(person1.name) # Zeynep
print(person1.age) # 21

person1.greeting() # Hi, my name is Zeynep.

# class Person: pass

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) # the child class inherit all the methods and properties from its parent

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

student1 = Student("Zey", "Ak")
student1.greeting() # Hi, my name is Zey.