
def merge(array):
	if len(array)>1:
		r = len(array)//2
		l = array[:r]
		m = array[r:]

		merge(l)
		merge(m)

		i=j=k=0
		while i<len(l) and j<len(m):
			if l[i]<m[j]:
				array[k] = l[i]
				i = i+1
			else:
				array[k] = m[j]
				j = j+1
			k = k+1

		while(i<len(l)):
			array[k] = l[i]
			k = k+1
			i = i+1
		while(j<len(m)):
			array[k] = m[j]
			k = k+1
			j = j+1



array=[7,1,-4,-5,-9,11,22,23,-10]
print("ARRAY:",array)

merge(array)

print("SORTED:",array)
