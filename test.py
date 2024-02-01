import numpy as np
# a = np.array([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29])
# val = int(input("Enter the value to be searched : "))
arr = np.array([[1,2,3],[3,4,5],[5,6,7]])

# def binary_search(a,val):
#     beg = 0
#     end  = len(a)-1
#     pos = 1
#     while beg<= end:
#         mid = int((beg+end)//2)
#         if a[mid] == val:
#             print(f"element found at {mid}")
#             pos = mid
#             break
#         elif a[mid]>val:
#             end = mid - 1
#         else:
#             beg = mid + 1
#     if pos == -1 :
#         print("Element not present in array")
# binary_search(a,val)
def transpose(arr):
    rows = len(arr)
    columns = len(arr[0])
    for i in range (0,rows-1):
        for j in range (0,columns - 1):
            if rows==columns:
                    temp = arr[i][j]
                    arr[i][j] = arr[j][i]
                    arr[j][i] = temp
                    print(arr)
                    break
            else:
                if rows!=columns:
                    temp = arr[i][j]
                    arr[i][j] = arr[j][i]
                    arr[j][i] = temp
                    if rows > columns:
                        temp = arr[i][j]
                        arr[i][j] = arr[j][i]
                        arr[j][i] = temp
                        print(arr)
                        break
                    else:
                        temp = arr[i][j]
                        arr[i][j] = arr[j][i]
                        arr[j][i] = temp
                        print(arr)
                        break
                    break
transpose(arr)