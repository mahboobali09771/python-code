count = 0
for i in range(5,0,-1):
    for j in range(i,0,-1):
        if i+j == 5:
            count +=1
            break
        else:
            count += i*j
print(count)