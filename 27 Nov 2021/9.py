a = [0, 1, 2, 3, 4]
b = [4, 1, 0, 3, 2]
c = [3, 2, 4, 1, 0]
for i in range(len(a)):
    k = a[i]
    a[i] = c[b[k]]
print(a)