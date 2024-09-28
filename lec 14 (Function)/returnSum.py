# write a function to accept 2 numbers as input and return sum
x,y = input("enter two numbers : ").split()
x = int(x)
y = int(y)
def add(x,y):
    return x+y
print("sum of two numbers is =",add(x,y))