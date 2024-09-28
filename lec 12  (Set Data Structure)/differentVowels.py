w = input("enter any string : ")
s = set(w)
v = {'a','e','i','o','u'}
d = s.intersection(v)
print("vowels present in string",d)