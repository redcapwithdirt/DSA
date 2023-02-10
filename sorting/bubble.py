def bubblesort(array):
	for i in range(len(array)):
		for j in range(0,len(array)-i-1):
			if(array[j]>array[j+1]):
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp

array = [10,-2,4,11,-3,23,-9]

print("ORIGINAL ARRAY:",end="")
print(array)

bubblesort(array)

print("SORTED ARRAY:",end="")
print(array)