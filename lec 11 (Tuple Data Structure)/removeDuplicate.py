# suppose a list contain 20 elements and some of them are duplicates wap to remove duplicate element from list
l = [1,1,4,5,6,7,4,6,5,3,6,8,5,3,5,7,0,1,3,6]
ans = []
print(len(l))
for i in l:
    if i not in ans:
     ans.append(i)
print(ans)
