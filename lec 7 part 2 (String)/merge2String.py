# wap to merge characters of 2 string into a single string by taking characters alternatively
s1 = "ravi"
s2 = "teja"
s = ""
i =0
l1 = len(s1)
l2 = len(s2)
while i<l1 and i<l2:
    s = s + s1[i] + s2[i]
    i += 1
print(s)
