class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class Doublylinked(node):
    def __init__(self):
        self.head = None
    def traverse(self):
        if self.head == None:
            print("Empty list....")
        elif self.head.next == self.head:
            print(self.head.data)
        else:
            print(self.head.data)
            PTR = self.head.next
            while PTR != self.head:
                print(PTR.data)
                PTR = PTR.next
    def reversetraverse(self):
        PTR = self.head.prev
        if self.head == None:
            print("Empty list....")
        elif self.head.prev == self.head:
            print(self.head.data)
        while PTR.prev != self.head:
            print(PTR.data)
            PTR = PTR.prev
    def insert_end(self,val):
        newnode = node(val)
        if self.head == None:
            self.head = newnode
        newnode.prev = self.head
        self.head.prev.next = newnode
        newnode.next = self.head    
        self.head.prev = newnode
        self.traverse()
    def insert_front(self,val):
        newnode = node(val)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.prev.next = newnode
            newnode.prev = self.head.prev    
            self.head.prev = newnode
        self.traverse()

link = Doublylinked()
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