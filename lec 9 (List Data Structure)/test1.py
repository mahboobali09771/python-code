# predict the output of this program
squares = [x*x for x in range(5)]
result = 0
for i in squares:
    if i>5:
        result +=i
        break
    result += i
else:
    result += 10
print(result) # 14