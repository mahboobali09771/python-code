a = 10
b = 10
c = 10
print(id(a)) # same location
print(id(b)) # same location
print(id(c)) # same location

c = 11
print(id(c)) # different location