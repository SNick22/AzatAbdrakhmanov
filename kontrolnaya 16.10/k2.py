A = [5,4,5,6,9,8,7,7,6,5,4,4,6,7,8,9,0]
m1 = 0
m2 = 0
m3 = 0
for i in range(len(A)):
    if A[i]>m1:
        m3 = m2
        m2 = m1
        m1 = A[i]
    elif A[i]>m2 and A[i] != m1:
        m3 = m2
        m2 = A[i]
    elif A[i]>m3 and A[i] != m1 and A[i] != m2:
        m3 = A[i]
print(m3)