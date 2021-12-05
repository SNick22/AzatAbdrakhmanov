n = [234234, 34637353, 456, 346357357, 12345, 666666, 222, 55555]
k = 0
for i in n:
    if len(str(i)) == 3 or len(str(i)) == 5:
        m = 0
        for l in str(i):
            if int(l) % 2 ==0:
                m +=1
        if m == len(str(i)) or m == 0:
            k += 1
if k == 2:
    print(True)
else:
    print(False)