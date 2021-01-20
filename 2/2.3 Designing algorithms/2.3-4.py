# Celso Uliana -- Jan 2021
# Recursive binary search python 3 

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 20]

def iterativeBinarySearch(A, x):
    l = m = 0
    h = len(A) - 1

    while l <= h:
        m = (l + h) // 2

        if x > A[m]:
            l = m + 1
        elif x < A[m]:
            h = m - 1
        else:
            return m
    return None

def recursiveBinarySearch(A, x, l, h):
    if l > h:
        return None
        
    m = (l + h) // 2

    if x == A[m]:
        return m
    elif x > A[m]:
        return recursiveBinarySearch(A, x, m + 1, h)
    else:
        return recursiveBinarySearch(A, x, l, m - 1)

print(recursiveBinarySearch(A, 20, 0, len(A) - 1))
print(iterativeBinarySearch(A, 20))