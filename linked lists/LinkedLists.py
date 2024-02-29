


class newnode:
    def __init__(self,data):
        self.data = data
        self.next = None




class LinkedLists(newnode):
    def __init__(self):
        self.head = None
        
    def traverse(self):
        PTR = self.head
        if self.head == None:
            print("\nNo elements")
        while PTR != None:
            print(PTR.data)
            PTR = PTR.next 

    def insert_front(self,val):
        node = newnode(val)
        node.next = self.head
        self.head = node
        self.traverse()

    def insert_end(self,val):
        node  = newnode(val)
        if self.head == None:
            self.head = node
        else:
            PTR = self.head
            while PTR.next!=None:
                PTR = PTR.next
            PTR.next = node
        self.traverse()

    def insert_after_num(self,num,val):
        node = newnode(val)
        if self.head == None:
            print("No elements")
        PTR = self.head
        while PTR.next!=None and PTR.data != num :
            PTR = PTR.next
        if PTR == None:
            print("Number not found")
        else:
            node.next = PTR.next
            PTR.next = node
        self.traverse()

    def delete_front(self):
        if self.head == None:
            print("No elements")
        else:
            self.head = self.head.next
        self.traverse()

    def delete_end(self):
        if self.head == None:
            print("No element")
        elif self.head.next == None:
            self.head = None
        PTR = self.head 
        PRE = self.head
        while PTR.next != None:
            PRE = PTR
            PTR = PTR.next
        PRE.next = None
        self.traverse()

    def delete_after_num(self,num):
        if self.head == None:
            print("No elements")
        PTR = self.head.next
        PRE = self.head
        while self.head != None and PRE.data != num:
            PRE = PTR
            PTR = PTR.next
        if PRE == None:
            print(f"{num} not found")
        elif PRE == self.head:
            self.head = self.head.next
        else:
            PRE.next = PTR.next
        self.traverse()

    
    
        
link = LinkedLists()
while (1):
    
    print("\n===========Linked list manager===========\n")
    print("1. Print the linked list")
    print("2. Insert value at the front")
    print("3. Insert value at the end")
    print("4. Insert value after a given value")
    print("5. Delete value at the front")
    print("6. Delete value at the end")
    print("7. Delete value after a given value")


    ch = int(input("\nEnter your choice : "))
    
    if ch == 1:
        link.traverse()
    elif ch == 2:
        val = int(input("Enter the value : "))
        link.insert_front(val)
    elif ch == 3:
        val = int(input("Enter the value : "))
        link.insert_end(val)
    elif ch == 4:
        num = int(input("Enter the number to insert after : "))
        val = int(input("Enter the value : "))
        link.insert_after_num(num,val)
    elif ch == 5:
        link.delete_front()
    elif ch == 6:
        link.delete_end()
    elif ch == 7:
        num = int(input("Enter the value after which you want to delete the element : "))
        link.delete_after_num(num)
    
        
 