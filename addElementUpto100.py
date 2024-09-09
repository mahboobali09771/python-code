# wap to add all elements to list upto 100 which is divisible by 10
# use append method [hint: range,if condition]
list = []
for i in range(1,101):
    if i%10==0:
        list.append(i)
print(list)