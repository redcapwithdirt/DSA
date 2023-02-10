class Node:
	def __init__(self,val):
		self.next = None 
		self.val= val 



def printlist(head):
	temp = head
	while(temp!=None):
		print(temp.val,end=" ")
		temp= temp.next
	print()

def reverse(head):
	current = head
	prev = None 
	while(current!=None):
		n = current.next
		current.next = prev
		prev = current 
		current = n
	head=prev
	return head

def addone(head):
	head=reverse(head)
	k = head
	carry = 0
	prev = None 
	head.val += 1
	while(head!=None) and (carry>0 or head.val>9):
		prev = head
		head.val += carry
		carry = head.val//10
		head.val = head.val%10
		head = head.next
	if(carry>0):
		prev.next = Node(carry)
	return(reverse(k))

head = Node(9)
head.next = Node(9)
head.next.next = Node(9)
head.next.next.next = Node(9)
printlist(head)
head = addone(head)
printlist(head)



