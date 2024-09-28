# write a recursive program to find factorial of given number
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(5,"! = ",fact(5))