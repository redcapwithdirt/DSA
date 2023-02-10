class Node:
	def __init__(self,data):
		self.data = data
		self.next = None 

class Circularll:
	def __init__(self):
		self.last = None 


	def addtoempty(self,data):
		if self.last!=None:
			return self.last
		new_node = Node(data)
		self.last = new_node
		self.last.next = self.last
		return self.last

	def addfront(self,data):
		if self.last == None:
			return self.last

		new_node = Node(data)
		new_node.next = self.last.next
		self.last.next = new_node
		return self.last

	def traverse(self):
		if(self.last == None):
			print("THE LIST IS EMPTY")
			return

		temp = self.last.next
		while temp:
			print(temp.data , end=" ")
			temp = temp.next
			if(temp == self.last.next):
				break
		print()



cll = Circularll()
last = cll.addtoempty(4)
last = cll.addfront(10)
last = cll.addfront(12)
last = cll.addfront(14)
cll.traverse()
