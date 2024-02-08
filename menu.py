# Create a menu driven program for arrays having access to:
# 1. Print the array 
# 2. Insert value at end 
# 3. Insert value at front
# 4. Insert value at a given index location 
# 5. Insert value after a given value
# 6. Search value in array



import numpy as np
class menu:
    def __init__(self,size):
        self.arr = np.zeros(size)
        self.N = 0
        self.size = size
    def traverse(self):
        if self.N == 0:
            print("Empty Array")
        else:
            for i in range(0,self.N):
                print(self.arr[i])
    def insert_front(self,val):
        if self.N==self.size:
            print("Array overflow")
        else:
            for i in range(self.N-1,-1,-1):
                self.arr[i+1]=self.arr[i]
            self.arr[0]=val
            self.N=self.N+1
            print("Element inserted at the front")
        for i in range(0,self.N):
                print(self.arr[i])
    def insert_end(self,val):
        if self.N==self.size:
            print("Array oveflow")
        else:
            self.arr[self.N]=val
            self.N=self.N+1
            print("Element inserted at the end")
        for i in range(0,self.N):
                print(self.arr[i])
    def insert_pos(self,val,pos):
        if self.N==self.size:
            print("Array overflow")
        else:
            if pos<0 or pos>self.N:
                print("Invalid input")
            elif pos==self.N:
                self.arr[pos]=val
                self.N=self.N+1
                print("Element inserted at the given position")
            else:
                for i in range(self.N-1,pos,-1): 
                    self.arr[i+1]=self.arr[i]
                self.arr[pos]=val
                self.N=self.N+1
                print("Element inserted at the given position")
        for i in range(0,self.N):
                print(self.arr[i])
    def insert_after_value(self, giv_val, val):
        indices = np.where(self.arr == giv_val)
        index = indices[0][0]
        if self.N==self.size:
            print("Array overflow")
        else:
            for i in range(self.N-1,index-1,-1):
                    self.arr[i+1] = self.arr[i]
            self.arr[index+1] = val   
            self.N = self.N+1
            print("Value replaced successfully")
        for i in range(0,self.N):
                print(self.arr[i])
    def search_val(self, val):
        indeces = np.where(self.arr == val)
        index = indeces[0]
        condition = False
        if self.N==self.size:
            print("Array overflow")
        else:
            for i in self.arr:
                if i == val:
                    condition = True
                    print(f"{i} found at index {index}")
                    break
        if(condition==False):
            print("Element not found")





# 2. Delete value at end

# 3. Delete value at front

# 4. Delete value at a given index location

# 5. Delete value after a given value



    def delete_end(self):
        if self.N == 0:
            print("Array underflow")
        else:
            self.N=self.N-1
        for i in range(0,self.N):
                print(self.arr[i])
    def delete_front(self):
        if self.N==0:
            print("Array underflow")
        else:
            for i in range(0,self.N-1):
                self.arr[i]=self.arr[i+1]
            self.N=self.N-1
        for i in range(0,self.N):
                print(self.arr[i])
    def delete_index(self,dex):
        if self.N==0:
            print("Array underflow")
        else: 
            for i in range(dex+1,self.N):
                self.arr[i-1]=self.arr[i]
            np.delete(self.arr, dex)
            self.N-=1
        for i in range(0,self.N):
                print(self.arr[i])
    def delete_givval(self,giv_val):
        indices = np.where(self.arr == giv_val)
        index = indices[0][0]
        if self.N==0:
            print("Array underflow")
        else:
            for i in range(index+2,self.N):
                self.arr[i-1]=self.arr[i]
            np.delete(self.arr, index+1)
            self.N-=1
        for i in range(0,self.N):
                print(self.arr[i])
<<<<<<< HEAD
                
                
                
# Bubble sort

# Insertion sort

# Selection sort

    def bubble_sort(self):
        for i in range(0,self.N-1):
            for j in range(0,self.N-i-1):
                if self.arr[j]>self.arr[j+1]:
                    temp = self.arr[j+1]
                    self.arr[j+1] = self.arr[j]
                    self.arr[j] = temp
        for i in range(0,self.N):
                print(self.arr[i])
                
    def insertion_sort(self):
        for i in range(1,self.N-1):
            key = self.arr[i]
            j = i - 1
            while j>0 and self.arr[j]>key:
                self.arr[j+1]=self.arr[j]
                j = j-1
            self.arr[j+1] = key
        for i in range(0,self.N):
                print(self.arr[i])
                    



=======
>>>>>>> 69d58ea796a500f224fa22201d1de041ee6b0b6a


size = 10
p = menu(size)
while(1):

    print("1. Print the elements in the array")
    print("2. Insert value at the end")
    print("3. Insert values at the front")
    print("4. Insert values at a position")
    print("5. Insert values at a given value")
    print("6. Search values in array")
    print("7. Delete values at the end")
    print("8. Delete values at the front")
    print("9. Delete values at a given index")
    print("10. Delete values after a given value")
<<<<<<< HEAD
    print("11. Bubble sort")
    print("12. insertion sort")
    print("13. Exit")
=======
    print("11. Exit")
>>>>>>> 69d58ea796a500f224fa22201d1de041ee6b0b6a
    


    ch=int(input("Enter your choice : "))

    if(ch==1):

        p.traverse()

    elif(ch==2):
        val = int(input("Enter your value : "))
        p.insert_end(val)
    elif(ch==3):
        val = int(input("Enter your value : "))
        p.insert_front(val)
    elif(ch==4):
        val = int(input("Enter your value : "))
        pos = int(input("Enter the index where you want to enter your value : "))
        p.insert_pos(val,pos)
    elif(ch==5):
        giv_val = int(input("Enter the value after which you want your new value : "))
        val = int(input("Enter the new value : "))
        p.insert_after_value(giv_val,val)
    elif(ch==6):
        val = int(input("Enter the element you want to search : "))
        p.search_val(val)
    elif(ch==7):
        p.delete_end()
    elif(ch==8):
        p.delete_front()
    elif(ch==9):
        dex = int(input("Enter index of the value to be deleted : "))
        p.delete_index(dex)
    elif(ch==10):
        giv_val = int(input("Enter the value after which you want to delete the element : "))
        p.delete_givval(giv_val)
    elif(ch==11):
<<<<<<< HEAD
        p.bubble_sort()
    elif(ch==12):
        p.insertion_sort()
    elif(ch==13):
        print("Exited successfully")
        break
    else:
        print("Invalid input!!")
=======
        print("Exited successfully")
        break
    else:
        print("Invalid input!!")
>>>>>>> 69d58ea796a500f224fa22201d1de041ee6b0b6a
