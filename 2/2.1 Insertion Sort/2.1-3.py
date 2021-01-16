# Celso Uliana -- Jan 2021
# Linear search

A = [5, 2, 4, 6, 1, 3]

def linearSearch(A, v):
    for i in range(len(A)):
        if A[i] == v:
            return i
    return None

print(linearSearch(A, 5))