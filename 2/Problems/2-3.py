# Celso Uliana -- Jan 2021
# Naive polynomial-evaluation python 3

#2x² + 3x + 1 x = 2 // 8 + 6 + 1 = 15
#a = [2, 3, 1]
#2x³ + 3x + 1 x = 2 // 16 + 6 + 1 = 23
#a = [2, 0, 3, 1]
#2x³ - 6x² + 2x - 1 x = 2 // 16 - 24 + 4 - 1 = -5
a = [2, -6, 2, -1]

# O(n²) naive polynomial evaluation
def naivePolynomialEvaluation(x, a):
    polySum = 0
    for i in range(len(a)):
        p = 1
        for _ in range(len(a) - i - 1):
            p = p * x
        polySum += a[i] * p
    return polySum

print(naivePolynomialEvaluation(2, a))