x = [10,20,255]
b = bytes(x)
print(type(b))
# b[0] = 21  # bytes is immutable
print(b[0])
for i in b:
    print(i)

''' # multiline comment

y = [10,20,256]  # byte is not allowed 256 values
c = bytes(y)
print(type(c))
print(c[0])
for j in c:
    print(j)

    '''