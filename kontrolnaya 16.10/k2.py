A = [11,43,43,14,16,17,17]
max1 = 0
max2 = 0
max3 = 0
for i in range(len(A)):
    if A[i] > max1:
        max1 = A[i]
for i in range(len(A)):
    if (A[i] > max2) and (A[i] != max1):
        max2 = A[i]
for i in range(len(A)):
    if (A[i] > max3) and (A[i] != max1) and (A[i] != max2):
        max3 = A[i]
print(max3)