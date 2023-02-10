class Node:
    def __init__(self,item):
        self.next = None
        self.val = item 
        
class LL:
    def __init__(self):
        self.head = None
        
    def printlist(self):
        temp = self.head
        while(temp!=None):
            print(temp.val,end=" ")
            temp = temp.next
        print()
    
    def delduplicate(self):
        temp = self.head
        while(temp!=None and temp.next != None):
            if(temp.val ==temp.next.val):
                temp.next = temp.next.next
            else:
                temp = temp.next
                
    
        
ll = LL()
ll.head=Node(1)
ll.head.next = Node(1)
ll.head.next.next = Node(1)
ll.head.next.next.next = Node(2)
ll.head.next.next.next.next = Node(2)
ll.head.next.next.next.next.next = Node(3)

print("LIST:")
ll.printlist()
print("DUPLICATES REMOVED:")
ll.delduplicate()
ll.printlist()




