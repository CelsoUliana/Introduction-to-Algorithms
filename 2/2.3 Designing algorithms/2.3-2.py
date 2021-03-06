# Celso Uliana -- Jan 2021
# Merge sort without sentinels python 3
import random

#A = [5, 2, 4, 6, 1, 3]
A = random.sample(range(0, 50), 10)

def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0 for i in range(n1)]
    R = [0 for i in range(n2)]

    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
        
    i = j = 0

    for k in range(p, r + 1):
        if i == n1:
            A[k] = R[j]
            j += 1
        elif j == n2:
            A[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1  

print(A)    
mergeSort(A, 0, len(A) - 1)
print(A)