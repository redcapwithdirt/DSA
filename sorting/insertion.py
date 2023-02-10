
def insertionsort(array):
	for step in range(1,len(array)):
		key = array[step]
		j = step-1

		while(j>=0 and key<array[j]):
			
			array[j+1] = array[j]
			j = j-1
		array[j+1] = key


array = [-3,10,22,3,12,-7]
print("ARRAY:",end=" ")
print(array)

insertionsort(array)

print("SORTED:",end=" ")
print(array)