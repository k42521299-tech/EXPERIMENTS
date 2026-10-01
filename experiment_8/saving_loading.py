#WAP for saving and loading numpy arrays
import numpy as np
a= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Saving the array to a file
np.save('array.npy', a)
# Loading the array from the file
l = np.load('array.npy')
print("Loaded Array:")
print(l)
