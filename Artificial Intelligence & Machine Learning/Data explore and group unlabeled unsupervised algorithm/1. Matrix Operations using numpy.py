import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix addition
print("\nAddition of A and B:")
print(A + B)

# Matrix subtraction
print("\nSubtraction of A and B:")
print(A - B)

# Matrix multiplication
print("\nMatrix multiplication:")
print(np.dot(A, B))

# Transpose
print("\nTranspose of A:")
print(A.T)

# Determinant
print("\nDeterminant of A:")
print(np.linalg.det(A))

# Inverse
print("\nInverse of A:")
print(np.linalg.inv(A))
