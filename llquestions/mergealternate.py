class Node:
	def __init__(self,data):
		self.next = None 
		self.data = data

class LL:
	def __init__(self):
		self.head1 = None
		self.head2 = None 

	def traverse(self):
		print("FIRST LIST")
		temp1 = self.head1
		while(temp1!=None):
			print(temp1.data, end=" ")
			temp1 = temp1.next
		print()

		print("SECOND LIST")
		temp2 = self.head2
		while(temp2!=None):
			print(temp2.data,end=" ")
			temp2 = temp2.next
		print()

	def mergealternate(self):
		first = self.head1
		second = self.head2
		while(first!=None and second!=None):
			second.next = first.next
			first.next = second
			first = first.next.next
			second = second.next
			

	
	
ll = LL()
ll.head1 =Node(1)
ll.head1.next = Node(2)
ll.head1.next.next = Node(3)

ll.head2 = Node(4)
ll.head2.next = Node(5)
ll.head2.next.next = Node(6)

ll.traverse()

ll.mergealternate()
ll.traverse()


