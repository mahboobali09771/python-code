# wap to print characters at odd position and even position for the given strign(write in two different ways using slice operator and step using while loop)
str = input("enter string ")
print("using while loop ")
l = len(str)
i = 0
s1 = ""
s2 = ""
while i<l:
    if(i%2==0):
        s1 = s1 + str[i]
    else:
        s2 = s2 + str[i]
    i += 1
print("even character is = ",s1)
print("odd character is = ",s2)
  
print("using slice operator ")
s3 = str[0:len(str):2]
s4 = str[1:len(str):2]
print("even character is = ",s3)
print("odd character is = ",s4)