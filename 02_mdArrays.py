import numpy as np

arr = np.array([['A', 'B', 'C', 'D'],['E', 'F', 'G', 'H']]) # 2D array 

print(arr[1][3]) # Chaining indexing to access 'H'

print(arr[1, 3]) # multidimensional indexing to access 'H'