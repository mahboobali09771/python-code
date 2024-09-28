# suppose a list contain positive and negative numbers then wap to create 2 different lists seperative numbers and negative numbers
l = [1,-4,5,6,7,-4,6,5,-3,6,8,-5,3,9,-7,1,3,-6]
count = 0
for i in l:
    if i<0:
        count += 1
print("total number of negative numbers = ",count)

