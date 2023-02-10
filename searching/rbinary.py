
def resbinary(array,x,low,high):
    if(low>high):
        return -1
    else:
        mid = low + (high-low)//2
        if(array[mid]==x):
            return mid
        elif(array[mid]<x):
            return resbinary(array,x,mid+1,high)
        else:
            return resbinary(array,x,low,mid-1)




array = [3, 4, 5, 6, 7, 8, 9]
x = 8

result = resbinary(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")