# Celso Uliana -- Feb (yay) 2021
# Find maximum subarray divide and conquer python 3
import math

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
#                                  [18, 20, -7, 12] -> maximum subarray/ sum = 43

#A = [ -2, -3, -70, -1]

def findMaxCrossingSubarray(A, low, mid, high):
    leftSum = -math.inf
    ssum = 0
    
    for i in range(mid, low - 1, -1):
        ssum += A[i]
        if ssum > leftSum:
            leftSum = ssum
            maxLeft = i
            
    rightSum = -math.inf
    ssum = 0
    
    for j in range(mid + 1, high + 1):
        ssum += A[j]
        if ssum > rightSum:
            rightSum = ssum
            maxRight = j
            
    return (maxLeft, maxRight, leftSum + rightSum)

def findMaxSubarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    mid = (low + high) // 2
    
    leftLow, leftHigh, leftSum = findMaxSubarray(A, low, mid)
    rightLow, rightHigh, rightSum = findMaxSubarray(A, mid + 1, high)
    crossLow, crossHigh, crossSum = findMaxCrossingSubarray(A, low, mid, high)

    if leftSum >= rightSum and leftSum >= crossSum:
        return (leftLow, leftHigh, leftSum)
    elif rightSum >= leftSum and rightSum >= crossSum:
        return (rightLow, rightHigh, rightSum)
    else:
        return (crossLow, crossHigh, crossSum)

print(findMaxSubarray(A, 0, len(A) - 1))