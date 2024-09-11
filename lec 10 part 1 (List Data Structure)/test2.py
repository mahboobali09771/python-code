data = [1,2,3]
for i in range(len(data)):
    x = data[i]
    for j in range(i+1,len(data)):
        y = data[j]
        if x+y==4:
            print(x*y) # 3