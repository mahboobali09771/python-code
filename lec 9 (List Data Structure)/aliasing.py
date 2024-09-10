x = [10,20,30,40,50]
y = x
print(x)
print(y)
print(id(x))
print(id(y))
y[1] = 777
print(x)
print(y)