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
    n = len(arr)
    m = len(arr1)
    if len(arr[0]) != len(arr1[0]):
        print("Matrices cannot be multiplied!")
    else:
        multiply = np.array([[0 for i in range(len(arr))] for j in range(len(arr[0]))])
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                for k in range(len(arr1)):
                    multiply[i][j] = multiply[i][j] + arr[i][k] * arr1[k][j]
        print(f"\nMultiplication of matrix \n{arr}\n and \n{arr1}\n is : \n{multiply}")
mul_matrix(arr,arr1)
