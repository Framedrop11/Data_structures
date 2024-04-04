import numpy as np
class stacks():
    def __init__(self,size):
        self.arr = np.zeros(size)
        self.top = -1
        self.size = size
    def traverse(self):
        if self.top == -1:
            print("\nEmpty Stack")
        else:
            for i in range(self.top,-1,-1):
                print(self.arr[i])
    def push(self,val):
        if self.top == self.size-1:
            print("Stack overflow")
        elif self.top < self.size-1:
            self.top += 1
            self.arr[self.top] = val
        self.traverse()
    def pop(self):
        if self.top == -1:
            print("Stack underflow")
        else:
            self.top -= 1
        self.traverse()
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print(f"The topmost element is : {self.arr[self.top]}")
    
            
        
        
size = 10
sobj = stacks(size)



while(1):
    print("\n============Stack Menu============\n")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Exit")
    
    ch=int(input("\nEnter your choice : "))

    if(ch==1):
        val = int(input("Enter your value : "))
        sobj.push(val)
    elif(ch==2):
        sobj.pop()
    elif(ch==3):
        sobj.peek()
    elif(ch==4):
        break
    else:
        print("Invalid input!!!!!")
        
    
            