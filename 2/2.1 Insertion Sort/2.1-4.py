# Celso Uliana -- Jan 2021
# Linear binary array add

A = [1, 1, 1, 1, 0, 0] # 60
B = [1, 0, 1, 0, 0, 1] # 41

def binaryAdd(A, B):
    
    # Initialize n + 1 bit array
    C = [0 for i in range(len(A) + 1)]
    carryOver = 0
    
    # Reverse iterate it with carry over
    for i in reversed(range(len(A) + 1)):
        j = i - 1
        C[i] = A[j] + B[j] + carryOver
        carryOver = 0
        if C[i] > 1:
            C[i] -= 2
            carryOver = 1
        
    C[0] = carryOver
        
    return(C)

print(binaryAdd(A, B))