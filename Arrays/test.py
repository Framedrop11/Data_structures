# Find transpose of a matrix.

# Find the sum of two matrices.

# Multiply two matrices.


import numpy as np

arr = np.array([[1,2,3],[3,4,5],[5,6,7]])
arr1 = np.array([[1,2,3],[3,4,5],[5,6,7]])

def transpose(arr):
    trans = np.array([[0 for i in range(len(arr))] for j in range(len(arr[0]))])
    for k in range(len(arr)):
        for l in range(len(arr[0])):
            trans[k][l] = arr[l][k]
    print(f"\nThe transpose of the matrix \n{arr}\n is : \n{trans}")
transpose(arr)

def sum_matrix(arr,arr1):
    sum = arr + arr1
    print(f"\nSum of matrix \n{arr}\n and \n{arr1}\n is : \n{sum}")
sum_matrix(arr,arr1)

def mul_matrix(arr,arr1):
    mul = arr * arr1
    print(f"\nMultiplication of matrix \n{arr}\n and \n{arr1}\n is : \n{mul}")
mul_matrix(arr,arr1)
