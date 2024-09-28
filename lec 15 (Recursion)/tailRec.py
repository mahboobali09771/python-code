def tail_rec(n):
    if(n==0):
        return
    else:
        print(n,end=" ")
        return tail_rec(n-1)
tail_rec(4)