# Celso Uliana -- Jan 2021
# Find within a set S if exists f1 and f2 so that f1 + f2 = x in O(nlogn) time

S = [6, 6, 7, 20, 40, 80, 21, 5, 1, 2, 3, 2, 9]

# this is O(2nlogn) which is still O(nlogn)
def findSetSum(S, x):
    # f1 + f2 = x
    # f2 = x - f1

    # This is O(nlogn)
    mergeSort(S, 0, len(S) - 1)
    
    # This is O(nlogn) - n times logn
    for i in range(len(S)):
        f1 = S[i]
        f2 = x - f1
        
        # This is O(logn)
        pos = recursiveBinarySearch(S, f2, 0, len(S) - 1)
        
        # Check if position found is not i itself
        if pos and pos is not i:
            return True
            
    return False

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

print(findSetSum(S, 12))