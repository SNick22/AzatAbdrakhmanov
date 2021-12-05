n = 123456
m1 = ''
for i in str(n):
    if int(i) % 2 != 0:
        m1 += i
m = int(m1)
print(m)