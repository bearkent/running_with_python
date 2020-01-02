import numpy as np

matrix = np.array([[1,3],
                   [5,7],
                   [9,11]])

print(matrix)
matrix2 = matrix*matrix
print(matrix2)
m=matrix[2,1]
m=m-9
matrix[2,1]=m
print(matrix)
                  

                        