# take input from keyword list of any 5 numbers and find the length without using len()
l = [int(x) for x in input("enter list ").split()]
count = 0
for i in l:
    count += 1
print("total number of element in list :",count)
print(type(l))