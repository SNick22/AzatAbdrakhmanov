r = []
a = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
for i in range (len(a)-9):
    b = a[i:10+i]
    k = 0
    for i in range(len(a)-9):
        if b == a[i:10+i]:
            k += 1
    if k != 1 and not(b in r):
        r.append(b)
print(r)