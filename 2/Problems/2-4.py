# Celso Uliana -- Jan 2021
# Merge sort modification to count number of inversions python 3
import math

A = [2, 3, 8, 6, 1] # Inversions -> (2, 1), (3, 1), (8, 6), (8, 1), (6, 1)

# Since it runs exactly like mergeSort with some aditional constant operations it is O(logn)
def mergeSortInvCounter(A, p, r):
    inv = 0
    if p < r:
        q = (p + r) // 2
        inv += mergeSortInvCounter(A, p, q)
        inv += mergeSortInvCounter(A, q + 1, r)
        inv += mergeInvCounter(A, p, q, r)
    return inv

def mergeInvCounter(A, p, q, r):
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

    i = j = inv = 0
    
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            # At this point everything between i and n1 is an inversion (n1 - i can be 0 which indicates no inversion)
            inv += n1 - i
            # Not needed, but lists the inversions(not same order as above since that list is in the order it appears)
            for z in range(i, n1):
                print("({}, {})".format(L[z], R[j - 1]))
    return inv
 
print("Inversion count is", mergeSortInvCounter(A, 0, len(A) - 1))