# Celso Uliana -- Jan 2021
# Insertion sort python 3 (nonincreasing order)
import random

#A = [5, 2, 4, 6, 1, 3]
A = random.sample(range(0, 50), 10)

def insertionSortDesc(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        # A[i] < key = Desc order / A[i] > key = Asc order
        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

print(A)    
insertionSortDesc(A)
print(A)