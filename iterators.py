# __iter__(), __next__()

mystr = "python"
myit = iter(mystr)
print(next(myit)) # p
print(next(myit)) # y
print(next(myit)) # t
print(next(myit)) # h
print(next(myit)) # o
print(next(myit)) # n

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

my_iterator_class = MyNumbers()
myiter = iter(my_iterator_class)
print(next(myiter)) # 1
print(next(myiter)) # 2
print(next(myiter)) # 3
print(next(myiter)) # 4
print(next(myiter)) # 5