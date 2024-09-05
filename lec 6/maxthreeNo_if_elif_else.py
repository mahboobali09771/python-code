# m1 
a = int(input("Enter first value "))
b = int(input("Enter second value "))
c = int(input("Enter third value "))
if a>b and a>c:
    print("biggest number is a =",a)
elif b>c and b>a:
    print("biggest number is b = ",b)
else:
    print("biggest number is c = ",c)


# m2
# a,b,c = [int(x) for x in input("enter three number").split()]
# if a>b and a>c:
#     print("biggest number is a =",a)
# elif b>c and b>a:
#     print("biggest number is b = ",b)
# else:
#     print("biggest number is c = ",c)



# m3
# a,b,c = [int(x) for x in input("enter three number").split()]
# if a>b and a>c:
#     maxi = a
# elif b>c and b>a:
#     maxi = b
# else:
#     maxi = c
# print("maximum number is = ",maxi)