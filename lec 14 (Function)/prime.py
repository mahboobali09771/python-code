a = input("enter the number you want to check : ")
a = int(a)
def prime(n,count):
    for i in range(1,n+1):
        if n%i==0:
            count += 1
    if count == 2:
        print(n," is the prime number ")
    else:
        print(n," is not prime numbers")
        
prime(a,0)
