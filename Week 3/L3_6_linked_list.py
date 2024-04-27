# Linked List
class Node:
    def __init__(self, v=None):
        self.value=v
        self.next=None

    def isempty(self):
        if self.value == None:
            return True
        else:
            return False

    # Appending to a list
    
l1=Node() #Empty List
l2=Node(5) #Singleton List

print(l1.isempty())
print(l2.isempty())
