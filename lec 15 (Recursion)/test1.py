def A(n):
    if n<=1:
        return
    else:
        print(n-3,end=" ")
        A(n-1)
        print(n-1,end=" ")
        A(n-2)
        print(n,end=" ")
        A(n-3)
        print(n-2,end=" ")
A(4)