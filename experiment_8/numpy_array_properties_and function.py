#WAP for numpy array properties and functions
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Array:")
print(a)
print("\nShape of array:", a.shape)
print("Number of dimensions:", a.ndim)
print("Number of elements:", a.size)
print("Data type:", a.dtype)

print("\nSum of elements:", np.sum(a))
print("Minimum element:", np.min(a))
print("Maximum element:", np.max(a))
print("Mean of elements:", np.mean(a))
print("Transpose of array:")
print(np.transpose(a))
print("Array reshaped to 1 row:")
print(a.reshape(1, 9))
