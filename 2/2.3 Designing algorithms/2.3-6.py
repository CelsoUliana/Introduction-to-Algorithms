# Celso Uliana -- Jan 2021
# Insertion sort with binary search to find correct position for j-th element python 3 (nondecreasing order)
import random

#A = [5, 2, 4, 6, 1, 3]
A = random.sample(range(0, 50), 10)

# Modification of iterativeBinarySearch to find where element x would go, if A is sorted
def binarySortSearch(A, x, l, h):
    while l < h:
        m = (l + h) // 2
        
        if x < A[m]:
            h = m
        else:
            l = m + 1
            
    return l

def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        pos = binarySortSearch(A, key, 0, j)
        while i >= pos:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
        

print(A)
insertionSort(A)
print(A)