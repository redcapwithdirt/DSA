class Node:
	def __init__(self,item):
		self.item = item 
		self.next = None


class Linkedlist:
	def __init__(self):
		self.head = None

	def printlist(self):
		temp = self.head
		while(temp!=None):
			print(temp.item,end=" ")
			temp = temp.next
		print()

	def insert_at_beginning(self,item):
		new_node = Node(item)
		new_node.next =  self.head
		self.head = new_node

	def insert_at_end(self,item):
		new_node = Node(item)
		temp = self.head
		while(temp.next!=None):
			temp = temp.next
		temp.next = new_node

	def insert_at_middle(self,item,pos):
		
		new_node = Node(item)
		temp = self.head
		while(pos>1):
			temp = temp.next
			pos = pos -1
		new_node.next = temp.next
		temp.next = new_node

	def delstart(self):
		self.head = self.head.next

	def delend(self):
		temp = self.head
		while(temp.next.next!=None):
			temp = temp.next
		temp.next = None 

	def delmiddle(self,pos):
		temp = self.head
		while(pos>1):
			temp = temp.next
			pos = pos -1
		temp.next = temp.next.next

	def reverse(self):
		prev = None 
		current = self.head
		while(current!=None):
			n = current.next
			current.next = prev
			prev = current
			current = n
		self.head = prev 




ll = Linkedlist()
ll.head = Node(1)
second = Node(2)
third = Node(3)

ll.head.next = second
second.next = third

ll.printlist()

ll.insert_at_beginning(10)
ll.insert_at_beginning(12)

ll.printlist()

ll.insert_at_end(100)
ll.insert_at_end(101)

ll.printlist()

ll.insert_at_middle(222,1)
ll.printlist()

ll.delstart()
ll.delstart()
ll.printlist()

ll.delend()
ll.printlist()

ll.delmiddle(1)
ll.printlist()

ll.insert_at_beginning(23)
ll.insert_at_beginning(44)
ll.printlist()

ll.reverse()
ll.printlist()








