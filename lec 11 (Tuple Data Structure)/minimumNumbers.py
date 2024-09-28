# take input from keyword list of any 5 numbers and find the gcd of all those numbers
l = [int(x) for x in input("enter list ").split()]
# minimum number
min = l[0]
for i in l:
    if i<min:
        min = i
print("minimum numbers = ",min)