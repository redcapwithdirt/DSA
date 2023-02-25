
def max_sum(array,n,k):

	maximum = array[0]

	for i in range(n-k+1):

		current = 0

		for j in range(k):
			current = current + array[i+j]

		maximum = max(current,maximum)

	return maximum 


array = [1,4,2,10,2,3,1,0,20]
k = 4
n = len(array)

print(max_sum(array,n,k))

