def max_sum(array,n,k):
    
    maximum = 0
    for i in range(k):
        maximum += array[i]
    
    res = maximum 
    for i in range(k,n):
        res = (res + array[i])-array[i-k]
        maximum = max(maximum,res)
    return maximum  
    
    
array = [1,4,2,10,2,3,1,0,20]
n = len(array)
k = 4
print(max_sum(array,n,k))
    