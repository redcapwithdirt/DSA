

def linearsearch(array,n,x):
	for i in range(0,n):
		if(array[i]==x):
			return i 

	return -1


array = [10,2,3,22,3,4,3,2]
n = len(array)
x = 3
result = linearsearch(array,n,x)
if(result == -1):
	print("Element not found")
else:
	print(result)
