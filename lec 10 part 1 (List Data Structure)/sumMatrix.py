n1 = [[1,2,3],[4,5,6],[7,8,9]]
n2 = [[4,6,4],[4,3,6],[7,5,0]]
print("first matrix is =  ")
for i in range(len(n1)):
    for j in range(len(n1[i])):
        print(n1[i][j],end=" ")
    print("")
print("second matrix is = ")
for i in range(len(n2)):
    for j in range(len(n2[i])):
        print(n2[i][j],end=" ")
    print("")

for i in range(len(n1)):
    for j in range(len(n1[i])):
        n1[i][j] = n1[i][j] + n2[i][j]

print("sum of  matrix is = ")
for i in range(len(n2)):
    for j in range(len(n2[i])):
        print(n1[i][j],end=" ")
    print("")