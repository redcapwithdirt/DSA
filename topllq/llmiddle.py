class Node:
	def __init__(self,data):
		self.next = None 
		self.data = data


def mid(head):
	fast = head
	slow = head
	while(fast!=None and fast.next!=None):
		fast = fast.next.next
		slow = slow.next
	return slow.data


def printlist(head):
	temp = head
	while(temp!=None):
		print(temp.data,end=" ")
		temp = temp.next
	print()



a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)
a.next.next.next.next=Node(5)
a.next.next.next.next.next = Node(6)
head = a 
printlist(head)
middle = mid(head)
print(middle)

