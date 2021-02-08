# Celso Uliana -- Feb (yay) 2021
# Strassen algorithm square matrix multiplication with size n power of 2

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

def matrixOperation(A, B, add):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j] if add else A[i][j] - B[i][j]
    return C

# Numpy pls? I copied and adapted this part from a blog, but too lazy to find the link... so props to the guy.
def matrixQuadrantSplitJoin(A, n, split, a11, a12, a21, a22):
    if split:
        for i in range(n):
            for j in range(n):
                a11[i][j] = A[i][j]
                a12[i][j] = A[i][j + n]
                a21[i][j] = A[i + n][j]
                a22[i][j] = A[i + n][j + n]
        return (a11, a12, a21, a22)
    else:
        for i in range(n):
            for j in range(n):
                A[i][j] = a11[i][j]
                A[i][j + n] = a12[i][j]
                A[i + n][j] = a21[i][j]
                A[i + n][j + n] = a22[i][j]
        return A

# Could be made f****** easier with numpy but wanted to keep it native python, so f*** me.
def strassen(A, B): 
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        C = [[0 for _ in range(n)] for _ in range(n)]
        n = n // 2

        a11 = [[0 for _ in range(n)] for _ in range(n)]
        a12 = [[0 for _ in range(n)] for _ in range(n)]
        a21 = [[0 for _ in range(n)] for _ in range(n)]
        a22 = [[0 for _ in range(n)] for _ in range(n)]
        b11 = [[0 for _ in range(n)] for _ in range(n)]
        b12 = [[0 for _ in range(n)] for _ in range(n)]
        b21 = [[0 for _ in range(n)] for _ in range(n)]
        b22 = [[0 for _ in range(n)] for _ in range(n)]
        
        matrixQuadrantSplitJoin(A, n, True, a11, a12, a21, a22)
        matrixQuadrantSplitJoin(B, n, True, b11, b12, b21, b22)
        
        # p1 = a11 * s1 // s1 = b12 - b22
        p1 = strassen(a11, matrixOperation(b12, b22, False))
        
        # p2 = s2 * b22 // s2 = a11 + a12
        p2 = strassen(matrixOperation(a11, a12, True), b22)
        
        # p3 = s3 * b11 // s3 = a21 + a22
        p3 = strassen(matrixOperation(a21, a22, True), b11)
        
        # p4 = a22 * s4 // s4 = b21 - b11
        p4 = strassen(a22, matrixOperation(b21, b11, False))
        
        # p4 = s5 * s6 // s5 = a11 + a22 // s6 = b11 + b22
        p5 = strassen(matrixOperation(a11, a22, True), matrixOperation(b11, b22, True))
        
        # p6 = s7 * s8 // s7 = a12 - a22 // s8 = b21 + b22
        p6 = strassen(matrixOperation(a12, a22, False), matrixOperation(b21, b22, True))
        
        # p7 = s9 * s10 // s9 = a11 - a21 // s10 = b11 + b12
        p7 = strassen(matrixOperation(a11, a21, False), matrixOperation(b11, b12, True))
        
        # For chained sum of matrices order does not matter. A + B = B + A.
        # For strassen(matrix multiplication) order does matter. That's why all s(Segments) have to be computed before.

        # c11 = p5 + p4 - p2 + p6 
        c11 = matrixOperation(matrixOperation(matrixOperation(p5, p4, True), p2, False), p6, True)

        # c12 = p1 + p2
        c12 = matrixOperation(p1, p2, True)

        # c21 = p3 + p4
        c21 = matrixOperation(p3, p4, True)

        # c22 = p5 + p1 - p3 - p7 
        c22 = matrixOperation(matrixOperation(matrixOperation(p5, p1, True), p3, False), p7, False)

        matrixQuadrantSplitJoin(C, n, False, c11, c12, c21, c22)
        return C

print(strassen(A, B))