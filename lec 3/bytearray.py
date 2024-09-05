x = [10,20,255]
ba = bytearray(x)
print(type(ba))
ba[0] = 11 # bytearray is mutable
for i in ba:
    print(i)
