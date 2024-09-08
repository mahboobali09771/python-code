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
