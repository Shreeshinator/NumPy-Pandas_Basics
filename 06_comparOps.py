import numpy as np

scores = np.array([91, 55, 78, 100, 73, 82 , 64]) # array of scores
print("Scores:", scores)


print(scores == 100, "Excellent") # element-wise comparison for equality
print(scores > 80, "Passed") # element-wise comparison for greater than
print(scores < 60, "Failed") # element-wise comparison for less than

scores[scores < 60] = 0 # setting scores less than 60 to 0 (failing scores)
print("Updated Scores:", scores)
