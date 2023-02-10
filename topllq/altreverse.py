class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
        
def printlist(head):
    temp = head
    while(temp!=None):
        print(temp.data,end=" ")
        temp = temp.next
    print()
    
def altreverse(head,k):
    current = head
    n = None
    prev = None
    count = 0
    while(current!=None and count<k):
        n = current.next
        current.next = prev
        prev = current
        current = n
        count = count + 1
    if(head!=None):
        head.next = current
    count = 0
    while(count<k-1 and current!=None):
        current = current.next
        count = count+1
    if(current!=None):
        current.next=altreverse(current.next,k)
    return prev
    
        
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
printlist(head)
res = altreverse(head,2)
printlist(res)

