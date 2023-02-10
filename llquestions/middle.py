class Node:
	def __init__(self,data):
		self.next = None 
		self.data = data

class LL:
	def __init__(self):
		self.head = None 

	def traverse(self):
		temp = self.head
		while(temp!=None):
			print(temp.data, end=" ")
			temp = temp.next
		print()

	def middle(self):
		fast = self.head
		slow = self.head
		while(fast!=None and fast.next!=None):
			fast = fast.next.next
			slow = slow.next
		return slow.data

ll = LL()
ll.head =Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)
ll.head.next.next.next.next.next = Node(6)

ll.traverse()
a=ll.middle()
print("the middle part element is ")
print(a)


