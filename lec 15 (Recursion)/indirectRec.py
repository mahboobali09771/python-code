def A(n):
    if n<=1:
        return
    else:
        B(n-2)
        print(n,end=" ")
        B(n-1)
        print(n-2,end=" ")
def B(n):
    if n<=1: 
        return
    else:
        print(n-3,end=" ")
        A(n-1)
        A(n-2)
print("A(4) is = ")
A(4)
print("\n")
print("B(4) is = ")
B(4)