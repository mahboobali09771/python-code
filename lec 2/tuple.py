a = [1,2,3,4,5]
b = (6,7,8,9,10)
print(type(b))
print(b)
print(b[1:5])

a[0]  = 2  # list is mutable we can update values
print(a)  
# b[0] = 2   # tuple is immutable we cannot update values