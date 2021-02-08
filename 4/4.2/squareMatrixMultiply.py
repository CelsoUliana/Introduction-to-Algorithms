# Celso Uliana -- Feb (yay) 2021
# Naive square matrix multiply O(n³)

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

def squareMatrixMultiplyijk(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# For languages like C the compiler can slightly optimize this variant, don't know about python. So I guess very language dependent.
# https://stackoverflow.com/questions/9888154/which-ordering-of-nested-loops-for-iterating-over-a-2d-array-is-more-efficient/9888269#9888269
def squareMatrixMultiplyikj(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

print(squareMatrixMultiplyikj(A, B))