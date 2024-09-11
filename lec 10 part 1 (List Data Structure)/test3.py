n = 4
result = 1
for i in range(1,n+1):
    for j in range(i,0,-1):
        result *= j
    result //= i
    print(result)
print("final output is = ",result)