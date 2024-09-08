# wap to check whether given number is prime or not ? (take input from keyboard & don't use inbuilt functions)
n = int(input("Enter any number "))
i = 1
count = 0
while i<=n:
    if(n%i==0):
        count +=1
    i += 1
    
if count==2:
    print(n,"is prime ")
else:
    print(n,"is not prime ")
    


