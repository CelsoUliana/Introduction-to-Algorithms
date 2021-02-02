# Celso Uliana -- Feb (yay) 2021
# Find maximum subarray iterative python 3
import math

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
#                                  [18, 20, -7, 12] -> maximum subarray/ sum = 43

#A = [-2, -3, -70, -1]

def findMaxCrossingSubarrayIterative(A):
    n = len(A)
    maxSum = ssum = -math.inf

    for i in range(n):
        tempHigh = i

        if ssum > 0:
            ssum += A[i]
        else:
            tempLow = i
            ssum = A[i]
        
        if ssum > maxSum:
            maxSum = ssum
            high = tempHigh
            low = tempLow
            
    return (low, high, maxSum)

print(findMaxCrossingSubarrayIterative(A))