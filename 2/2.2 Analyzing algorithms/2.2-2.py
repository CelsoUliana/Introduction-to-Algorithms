# Celso Uliana -- Jan 2021
# Selection sort python 3
import random

#A = [5, 2, 4, 6, 1, 3]
A = random.sample(range(0, 50), 10)

def selectionSort(A):
    for i in range(len(A) - 1):
        mi = i
        for j in range(i + 1, len(A)):
            if A[j] < A[mi]:
                mi = j
        A[i], A[mi] = A[mi], A[i]

print(A)
selectionSort(A)
print(A)