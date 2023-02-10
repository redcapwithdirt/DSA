
def selectionsort(array):
	size = len(array)
	for step in range(size):
		m = step
		for j in range(step+1,size):
			if(array[j]<array[m]):
				m = j
		array[step],array[m] = array[m],array[step]


array = [-3,-4,11,23,3,-9]

print("ORIGINAL ARRAY:",end="")
print(array)

selectionsort(array)

print("SORTED ARRAY:",end="")
print(array)
