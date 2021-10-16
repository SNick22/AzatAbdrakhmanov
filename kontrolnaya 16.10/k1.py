A = [1,3,3,4,6,7]
B = [4,4,6,7,8,9,10]
res = []
k1 = 0
k2 = 0
while len(res) != len(A) + len(B):
    if k1 > len(A)-1:
        res.append(B[k2])
        k2+=1
    elif k2 > len(B)-1:
        res.append(A[k1])
        k1+=1
    elif A[k1] < B[k2]:
        res.append(A[k1])
        k1+=1
    elif A[k1] == B[k2]:
        res.append(A[k1])
        res.append(B[k2])
        k1+=1
        k2+=1
    elif A[k1] > B[k2]:
        res.append(B[k2])
        k2+=1
print(res)