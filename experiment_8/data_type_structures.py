#WAP for data type structures in numpy
import numpy as np

a = np.array([1, 2, 3])
b = np.array([1.5, 2.5, 3.5])
c = np.array(["A", "B", "C"])
d = np.array([True, False, True])

print("Integer array:", a)
print("Data type:", a.dtype)

print("\nFloat array:", b)
print("Data type:", b.dtype)

print("\nString array:", c)
print("Data type:", c.dtype)

print("\nBoolean array:", d)
print("Data type:", d.dtype)

print("\n1-D Array:")
print(np.array([1, 2, 3]))

print("\n2-D Array:")
print(np.array([[1, 2], [3, 4]]))

print("\n3-D Array:")
print(np.array([[[1, 2], [3, 4]]]))