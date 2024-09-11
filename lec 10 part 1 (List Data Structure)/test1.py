# what is the output printed 
values = [1,2,3,4,5]
total = 0
for i in values:
    total +=i
    if total>10:
        total -= i
        break
    total +=i
print(total) # 12