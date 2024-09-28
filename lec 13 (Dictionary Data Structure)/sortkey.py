# wap to display all key value pairs of dictionary a/c to ascending of key
d = {100:'mahboob',500:'ali',200:'mohammad',600:'hello'}
for key,value in sorted(d.items()):
    print(key,"--",value)