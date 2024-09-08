# wap display the sum of first n numbers using while loop take n value as input from keyword
n = int(input("Enter n value "))
i = 1
sum = 0
while i<=n:
    sum += i
    i += 1
print("sum of number is = ",sum)