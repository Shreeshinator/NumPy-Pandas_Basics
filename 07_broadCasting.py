import numpy as np

# Broadcasting in numpy allows operations to be performed on arrays of different shapes and sizes without the need for explicit loops.

# This can only be done if the shapes of the arrays are compatible for broadcasting. The rules for broadcasting are as follows:
# 1. If the arrays have different numbers of dimensions, the shape of the smaller array
# 2. If the shape of the arrays does not match in any dimension, the array with a shape of 1 in that dimension is stretched to match the other shape.
# 3. If the shapes of the arrays do not match and neither has a shape of 1 in any dimension, an error is raised.

array1 = np.array([[1, 2, 3, 4]]) # 1D array
array2 = np.array([[1], [2], [3], [4]]) # 2D array

print(array1.shape) # Shape of array1 (rows, columns)
print(array2.shape) # Shape of array2 (rows, columns)

print(array1 * array2) # Broadcasting multiplication of array1 and array2

