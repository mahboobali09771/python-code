x = [1,2,4,5,6,9]
y = x.copy()
y[1] = 999
print(x)
print(y)
print(id(x))
print(id(y))