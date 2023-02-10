class Node:
	def __init__(self,item):
		self.next = None 
		self.prev = None 
		self.item = item 

class Dlist:
	def __init__(self):
		self.head = None 

	def printlist(self):
		temp = self.head
		while(temp!=None):
			print(temp.item, end=" ")
			temp = temp.next
		print()

	def printreverse(self):
		temp = self.head
		while(temp.next!=None):
			temp = temp.next
		while(temp!=None):
			print(temp.item,end=" ")
			temp = temp.prev 
		print()

	def addatbeg(self,item):
		new_node = Node(item)
		new_node.next = self.head
		self.head.prev = new_node
		self.head = new_node

	def addatend(self,item):
		new_node = Node(item)
		temp = self.head
		while(temp.next != None):
			temp=temp.next
		temp.next = new_node
		new_node.prev = temp

dll = Dlist()
dll.head = Node(10)
second = Node(20)
third = Node(30)
dll.head.next = second
second.next = third

second.prev = dll.head
third.prev = second

dll.printlist()
# dll.printreverse()
dll.addatbeg(121)
dll.addatbeg(111)

dll.printlist()

dll.addatend(200)
dll.addatend(201)

dll.printlist()
print("print in revese order")
dll.printreverse()



