# predict the outpur of the program(this program is also known as fibonacci series)
a =0
b =1
list = []
for i in range(6):
    a,b = b,a+b
    list.append(a)
    # print(a,end=" ") # fiboncci sequence
# print("\n")
print(sum(x for x in list if x%2==0))