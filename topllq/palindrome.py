class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

def pal(head):
    slow = head
    stack = []
    while(slow!=None):
        stack.append(slow.data)
        slow = slow.next
    ispalin = False
    # print(stack)
    while(head!=None):
        i = stack.pop()
        # print(i)
        if(head.data==i):
            ispalin = True
        else:
            ispalin = False
            break
        head = head.next
    return ispalin

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
res = pal(head)
print(res)


