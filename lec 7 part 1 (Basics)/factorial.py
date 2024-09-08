# wap to print factorial of given number ?
n = int(input("enter number "))
fact = 1
i = 1
if n==0: fact = 1
while i<=n:
    fact *= i
    i += 1
print("factorial of ",n,"is = ",fact)