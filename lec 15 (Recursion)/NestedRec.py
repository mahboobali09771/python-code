def A(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return A(m - 1, 1)
    else:
        return A(m - 1, A(m, n - 1))

result = A(1, 5)
print(result)
result2 = A(2,3)
print(result2)
result3 = A(3,3)
print(result3)
result4 = A(3,2)
print(result4)