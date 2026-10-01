#WAP for nd array object, indexing and slicing
import numpy as np

# Creating ndarray object
a = np.array([10, 20, 30, 40, 50])

print("Array:", a)
print("Type:", type(a))

# Indexing
print("\nIndexing:")
print("First element:", a[0])
print("Third element:", a[2])
print("Last element:", a[-1])

# Slicing
print("\nSlicing:")
print("First three elements:", a[0:3])
print("Elements from index 2:", a[2:])
print("Every second element:", a[::2])
