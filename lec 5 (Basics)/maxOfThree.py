# wap to read 3 integer from keyboard and find maximum of 3 numbers  using ternary operator [hint : and]

# a = int(input("enter 1st value"))
# b = int(intput("enter 2nd value"))
# c = int(input("enter 3rd value"))
a,b,c = [int(x) for x in input("enter three numbers ").split()]
maxi=a if a>b and a>c else (b if b>c else c)
print("max value is = ",maxi)