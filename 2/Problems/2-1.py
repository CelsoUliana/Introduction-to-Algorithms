# Celso Uliana -- Jan 2021
# Merge-insertion sort python 3
import math
import random

#A = [5, 2, 4, 6, 1, 3]
A = random.sample(range(0, 50), 10)
k = 7

def insertionSort(A, p, r):
    for j in range(p, r + 1):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

def mergeSort(A, p, r):
    # if vector sort size is less than k, then sort using insertion sort
    if k >= r - p:
        insertionSort(A, p, r)
    else:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0 for i in range(n1 + 1)]
    R = [0 for i in range(n2 + 1)]

    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
        
    L[n1] = math.inf
    R[n2] = math.inf

    i = j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1  

print(A)    
mergeSort(A, 0, len(A) - 1)
print(A)