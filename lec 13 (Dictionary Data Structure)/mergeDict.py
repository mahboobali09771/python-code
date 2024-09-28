# wap to create 3 different dictionaries and concatenate (merge) them into  fourth dictionaries
d1 = {1:'mahboob',2:'ali'}
d2 = {3:'hello',4:'world'}
d3 = {5:'bill',6:'elon'}
d4 = {}
d4.update(d1)
d4.update(d2)
d4.update(d3)
print(d4)
