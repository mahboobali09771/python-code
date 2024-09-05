print("list")
l1 = [1,2,3]  # in list same content but different address
l2 = [1,2,3]  # in list same content but different address
print(id(l1),id(l2))
print(l1 is l2)
print(l1 == l2)
print(l1 is not l2)
print("no list ")
a = 10
b = 10
print(id(a),id(b))
print(a is b)
print(a == b)
print(a is not b)
