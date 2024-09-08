# wap to print all prime numbers from 1 to 300 and print total (count) how many prime numbers available ? (don't use inbuilt functions)
n = 300
i = 1
while i<=n:
    j=1
    count = 0
    while j<=i:
        if(i%j==0):
            count +=1
        j += 1
    if count==2:
            print(i)      
    i += 1


    


