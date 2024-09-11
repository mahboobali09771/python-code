s = [x*x for x in range(1,11)]
print(s)
v = [2**x for x in range(1,6)]
print(v)
m = [x for x in s if x%2==0]
print(m)


words = ["Bhanu","Naresh","Vental","chetan"]
l = [w[0] for w in words]
print(l)

num1 = [10,20,30,40]
num2 = [30,40,50,60]
num3 = [i for i in num1 if i not in num2]
print(num3)
# common elements present in num1 and num2
num4 = [i for i in num1 if i in num2]
print(num4)