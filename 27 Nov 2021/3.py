n = 1234
s = []
for i in str(n):
    s.insert(0, int(i))
for i in range(len(s)):
    if s[i] %2 != 0:
        s[i] = -s[i]
print(sum(s))