# write a function to accept 2 numbers as input and return multiplication
x,y = input("enter two numbers : ").split()
x = int(x)
y = int(y)
def mul(x,y):
    return x*y
print("multiplication of two numbers is =",mul(x,y))