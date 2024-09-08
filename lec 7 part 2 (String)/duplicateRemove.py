# wap to remove duplicate characters from the given input string (hint : use list ,for,if,append,join)
s = "abcdabbcdabbbcccddeeef"
ans = []
for char in s:
    if char not in ans:
        ans.append(char)
res = ' '.join(ans)
print(res)