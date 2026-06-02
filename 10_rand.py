import numpy as np
import os

rng = np.random.default_rng() # Create a random number generator object
np.integer  = rng.integers(1, 7) # Generate a random integer between 1 and 10
int_array = rng.integers(1, 10, size=(3, 4)) # Generate a 3x4 array of random integers between 1 and 10
print("Random integer:", np.integer) # Print the random integer
print("Integer array:", int_array) # Print the integer array

# For random floats, we can use the random method of the generator
float_number = rng.random() # Generate a single random float between 0 and 1
print("Random float:", float_number) # Print the random float

float_array = rng.random(size=(2, 5)) # Generate a 2x5 array of random floats between 0 and 1   
print("Random float array:", float_array) # Print the random float array
