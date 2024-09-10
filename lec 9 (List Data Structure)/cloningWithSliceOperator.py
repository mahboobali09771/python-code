x = [10,20,30,49]
y = x[:]
y[1] = 10000
print(x)
print(y)
print(id(x))
print(id(y))