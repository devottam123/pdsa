# Linked List
class Node:
    # L = []
    def __init__(self, v=None):
        self.value=v
        self.next=None
        return
    # Empty
    def isempty(self):
        if self.value == None:
            return True
        else:
            return False

    # Append
    def append(self,x):
        # If current node is empty
        if self.isempty(): 
            self.value = x
        # If current node is last node of the list 
        elif self.next == None:
            self.next = Node(x)
        # Else reverse to next node
        else:
            self.next.append(x) 
        return

    # iterative append
    def appendi(self, x):
        # 1) empty list 
        if self.isempty():
            self.value = x
            return
        # 2) Traverse the list to find the last node
        temp=self
        while temp.next!=None:
            temp=temp.next
        new=Node(x)
        temp.next=new
    # Insert
    def insert(self, x):
        # 1) empty list
        if self.isempty():
            self.value=x
            return
        # 2) insert at first position
        new=Node(x)
        (new.value,self.value)=(self.value,new.value)
        new.next=self.next
        self.next=new

    # Remove
    def remove1(self, x):
        # 0) If list is empty
        if self.isempty():
            return
        # 1) single value
        if self.value==x and self.next==None:
            self.value=None
            return
        # 2) removing first element in the list
        if self.value==x and self.next!=None:
            (self.value, self.next.value) = (self.next.value, self.value)
            self.next=self.next.next
            return
        # 3) x is not the first value
        if self.next!=None:
            # x is the last element
            if self.next.value == x and self.next.next==None:
                self.next=None
                return 
            self.next.remove(x)

    # Correct remove
    def remove2(self,x):
        # If list is empty
        if self.isempty():
            return
        # If v is the current node of the list
        if self.value==x:
            self.value=None
            if self.next!=None:
                self.value=self.next.value
                self.next=self.next.next
            return
        # If v is not the current node of the list, take the head pointer to that point where v is the current node of the list
        else:
            if self.next!=None:
                self.next.remove2(x)
                if self.next.value==None:
                    self.next=None

    def display(self):
        if self.isempty():
            print("None")
        else:
            temp=self
            while temp!=None:
                print(temp.value, end=" ")
                temp=temp.next

list=Node()
list.display()
list.append(10)
list.display()
print()
list.append(20)
list.display()
print()
list.append(30)
list.display()
print()
list.append(40)
list.display()
print()
list.appendi(50)
list.display()
print()
list.remove2(50)
list.display()
print()
list.remove2(20)
list.display()
print()




        


    # Appending to a list
    # Empty
    # L = []
    # L.append(1) #[1]
    # L.append(2) #[1, 2]
    # L.insert(0, 3) #[3, 1, 2]
    # L.remove(2)   #[3, 1]
    # print(L)


    
# l1=Node() #Empty List
# l2=Node(5) #Singleton List

# print(l1.isempty())
# print(l2.isempty())
