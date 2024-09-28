# take input from keyword list of any 5 numbers and find the gcd of all those numbers
l = [int(x) for x in input("enter list ").split()]
# length count of list
count = 0
for i in l:
    count +=1
# minimum number
min = l[0]
for i in l:
    if i<min:
        min = i
# finding gcd
for i in range(min,0,-1):
    count1 = 0 # temp count
    for j in l:
       if j%i==0:
           count1 += 1
    if count==count1:
        print("gcd is = ",i)
        break

