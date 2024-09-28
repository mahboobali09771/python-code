# print sorted order of elements in set (ascending order) don't use any sort function

A = {10,-1,3,6,18,20,31,70}
while A:
    min_A = min(A)
    print(min_A,end=" ")
    A.remove(min_A)
print(type(A))