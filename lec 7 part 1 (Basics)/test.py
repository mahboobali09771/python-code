result = 1
for i in range(3,6):
    result *= i
    for j in range(2,i):
        if i%j==0:
            result -= j
print(result)