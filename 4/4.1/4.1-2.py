# Celso Uliana -- Feb (yay) 2021
# Find maximum subarray brute force python 3
import math

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
#                                  [18, 20, -7, 12] -> maximum subarray/ sum = 43

def findMaxSubarrayBruteForce(A):
    maxSum = -math.inf
    n = len(A)

    for i in range(n):
        ssum = 0
        for j in range(i, n):
            ssum += A[j]
            if ssum > maxSum:
                maxSum = ssum
                low = i
                high = j
    return (low, high, maxSum)

print(findMaxSubarrayBruteForce(A))
