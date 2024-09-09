# wap to print all unique combination of 1,2,3 not to repeat any digit (111 222 333 not allowed)
i = 1
while i<=3:
    j=1
    while j<=3:
        k = 1
        while k<=3:
            if i==j or j==k or k==i:
                k += 1
                continue
            else:
                print(i,j,k)
            k += 1
        j += 1
    i += 1
'''
digits = [int(x) for x in input("enter 3 digits ").split()]
l = len(digits)
i = 0
print("length of digits is = ",l)
count = 0
while i<3:
    j=0
    while j<3:
        k=0
        while k<3:
            if i!=j and i!=k and j!=k :
                print(digits[i],digits[j],digits[k])
                count +=1
            k += 1
        j += 1
    i += 1
print("total possible combination ",count)
'''