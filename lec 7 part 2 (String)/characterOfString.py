# wap to print each character of string in forward and backward direction by using while loop
s = "mahboob"
i = 0
print("in forward direction ")
while i<len(s):
    print(s[i]) 
    i += 1
j = -1
print("in backward direction ")
while j>(-(len(s)+1)):
    print(s[j])
    j -= 1