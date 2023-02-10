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

	def removeduplicate(self):
		temp = self.head
		while(temp!=None and temp.next!=None):
			if(temp.data == temp.next.data):
				temp.next = temp.next.next
			else:
				temp = temp.next
	
ll = LL()
ll.head =Node(1)
ll.head.next = Node(1)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(4)
ll.head.next.next.next.next.next = Node(6)

ll.traverse()
ll.removeduplicate()
ll.traverse()

