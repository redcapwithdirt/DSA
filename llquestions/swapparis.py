class ListNode:
	def __init__(self,data):
		self.data =data
		self.next = None

def printlist(ll):
	temp = ll
	while(temp!=None):
		print(temp.data,end=" ")
		temp = temp.next
	print()

def swaptoparis(head):
	if(head == None or head.next ==None):
		return head

	dummy = ListNode(0)
	dummy.next = head
	prev = dummy
	cur = head

	while(cur and cur.next):
		prev.next = cur.next
		cur.next = prev.next.next
		prev.next.next = cur

		prev = cur
		cur = cur.next
	return dummy.next


ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)

print("BEFORE SWAPPING")
printlist(ll)

ll = swaptoparis(ll)
print("AFTER SWAPPING")
printlist(ll)

