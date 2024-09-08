#  wap to print all unique combination of 1,2,3,4 not to repeat any digit (1111 2222 3333 4444 not allowed)
digits = [int(x) for x in input("enter 4 digits ").split()]
l = len(digits)
i = 0
count = 0
print("length of digits is = ",l)
while i<l:
    j=0
    while j<l:
        k=0
        while k<l:
            m =0
            while m<l:
                if i!=j and i!=k and i!=m  and j!=k and j!=m and k!=m :
                     print(digits[i],digits[j],digits[k],digits[m])
                     count +=1
                m += 1
            k += 1
        j += 1
    i += 1

print("total possible combination = ",count)
