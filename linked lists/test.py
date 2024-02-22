<<<<<<< HEAD
print("hello world")
=======
import numpy as np
arr = np.array([[1,2,3],[3,4,5],[5,6,7]])
def transpose(arr):
    trans = np.array([[0 for i in range(len(arr))] for j in range(len(arr[0]))])
    for k in range(len(arr)):
        for l in range(len(arr[0])):
            trans[k][l] = arr[l][k]
    print(f"The transpose of the matrix \n{arr}\n is : \n{trans}")
<<<<<<< HEAD
transpose(arr)
=======
transpose(arr)

>>>>>>> 69d58ea796a500f224fa22201d1de041ee6b0b6a
>>>>>>> 511dff113cb4a1344e1afc8e1f2c3a1e5fb0e52f
