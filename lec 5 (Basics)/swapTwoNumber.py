# write a program to swap two numbers don't use third variable and don't use arithmetic operations
a,b = [int(x) for x in input("enter any two values ").split()]
print("Before swaping ")
print(a)
print(b)
print("After swaping")
b,a = a,b
print("a = ",a)
print("b = ",b)
