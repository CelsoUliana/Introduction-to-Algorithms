# Celso Uliana -- Feb (yay) 2021
# Naive recursive square matrix multiply O(n³) (n must be power of 2)

# Should result in [[4, 4], [10, 8]]
#A = [[1, 2], [3, 4]]
#B = [[2, 0], [1, 2]]

# Should result in [[2, 4], [7, 10]]
#A = [[2, 0], [1, 2]]
#B = [[1, 2], [3, 4]]

# Should result in [[96, 68, 69, 69], 
#                   [24, 56, 18, 52], 
#                   [58, 95, 71, 92],
#                   [90, 107, 81, 142]]
A = [[5, 2, 6, 1], [0, 6, 2, 0], [3, 8, 1, 4], [1, 8, 5, 6]]
B = [[7, 5, 8, 0], [1, 8, 2, 6], [9, 4, 3, 8], [5, 3, 7, 9]]

# Sums it and put it in the correct quadrant of the matrix.
def addMatrix(A, B, C, rC, cC):
    n = len(A)
    for i in range(n):
        for j in range(n):
            C[i + rC][j + cC] = A[i][j] + B[i][j]

# Unlike strassen this can be made via index manipulation.
def squareMatrixMultiplyRecursive(A, B, rA, cA, rB, cB, n):
    C = [[0 for _ in range(n)] for _ in range(n)]

    if n == 1:
        C[0][0] = A[rA][cA] * B[rB][cB]
    else:
        n = n // 2
        
        # cA = left / cA + n = right / rA = top / rA + n = bottom
        # So the get the Quadrant (cA, rA) = top left / (cA + n, rA) = top right
        # (cA, rA + n) = bottom left / (cA + n, rA + n) = bottom right   
        addMatrix(  squareMatrixMultiplyRecursive(A, B, rA, cA, rB, cB, n),                 # a11 * b11 +
                    squareMatrixMultiplyRecursive(A, B, rA, cA + n, rB + n, cB, n),         # a12 * b21 =
                    C, 0, 0)                                                                # c11
        addMatrix(  squareMatrixMultiplyRecursive(A, B, rA, cA, rB, cB + n, n),             # a11 * b12 + 
                    squareMatrixMultiplyRecursive(A, B, rA, cA + n, rB + n, cB + n, n),     # a12 * b22 =
                    C, 0, n)                                                                # c12
        addMatrix(  squareMatrixMultiplyRecursive(A, B, rA + n, cA, rB, cB, n),             # a21 * b11 +
                    squareMatrixMultiplyRecursive(A, B, rA + n, cA + n, rB + n, cB, n),     # a22 * b21 =
                    C, n, 0)                                                                # c21
        addMatrix(  squareMatrixMultiplyRecursive(A, B, rA + n, cA, rB, cB + n, n),         # a21 * b12 +
                    squareMatrixMultiplyRecursive(A, B, rA + n, cA + n, rB + n, cB + n, n), # a22 * b22 =
                    C, n, n)                                                                # c22
    return C

print(squareMatrixMultiplyRecursive(A, B, 0, 0, 0, 0, len(A)))