def square(l):
    for e in l:
        yield e*e

l = [1,2,3]
g = square(l)
print(next(g)) # 1
print(next(g)) # 4
print(next(g)) # 9

g = square(l)
for res in g:
    print(res)

g = square(l)
print(list(g))
