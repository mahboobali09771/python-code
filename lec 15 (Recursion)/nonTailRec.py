def nt(n):
    if n<=1:
        return
    else:
        nt(n-2)
        print(n,end=" ")
        nt(n-1)
        print(n-2,end=" ")
nt(4)