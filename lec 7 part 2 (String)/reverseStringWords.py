# wap to reverse order of words input[Learning python is very easy] ouput[easy very is python Learning]
# hint(use split() method and add the words in list in reverse way then add them in empty string using join)
s = "Learning python is very easy"
s = s.split()
print("before reverse",s)
reverse = ""
l = len(s) - 1
while l>=0:
    reverse = reverse + s[l] +" "
    l -= 1
print(reverse)


# 2nd method without add
'''
s = "Learning python is very easy"
s = s.split()
i = -1
while i>-(len(s)+1):
    print(s[i],end=" ")
    i -= 1
    '''