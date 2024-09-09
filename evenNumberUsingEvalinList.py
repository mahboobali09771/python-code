# wap to read list from keyboard using eval() functions,numbers from 1 to 10, and print only even numbers on screen
# Reading a list of numbers from the keyboard using eval()
numbers = eval(input("Enter a list of numbers from 1 to 10: "))
for i in numbers:
    if i%2==0:
        print(i,end=" ")
