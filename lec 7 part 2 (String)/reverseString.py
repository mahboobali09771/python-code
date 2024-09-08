# wap to reverse the given string using while loop (don't use slice operator or join)
s = input("Enter your string ")
l = len(s)-1
str = ""
while l>=0:
    str = str + s[l]
    l -= 1
print(str)