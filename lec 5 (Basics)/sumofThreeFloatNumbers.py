# write a program to read 3 float numbers from the keyboard with print their sum
a,b,c = [float(x) for x in input("enter three numbers ").split()]
print("sum of three float numbers is = ",a+b+c)