# wap to read 4 integer from keyboard and find minimum of 4 numbers  using ternary operator [hint : and]
a,b,c,d = [int(x) for x in input("enter four numbers ").split()]
minimum = a if a<b and a<c and a<d else (b if b<c and b<d else (c if c<d else d))
print("minimum is = ",minimum)