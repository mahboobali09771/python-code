# wap to read 10 to 20 numbers from keyboard using eval() fun in the form of list and print those elements along with index number.

l = eval(input("Enter a list of numbers from 10 to 20: "))
x = len(l)
for i in range(x):
        print(l[i],"is available at positive index :",i,"and at negative index : ",i-x)