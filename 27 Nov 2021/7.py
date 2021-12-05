n = 123495678
n1 = str(n)
k = 0
for i in n1:
    if int(i) > k:
        k = int(i)
print(k)