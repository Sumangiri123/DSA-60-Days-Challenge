def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] < pivot :
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1 

def quick_sort(arr,low,high):
    if low >= high:
        return
    pi = partition(arr,low,high) # O(n)
    quick_sort(arr,low,pi-1) # O(log n)
    quick_sort(arr,pi+1,high) # O(log n)


arr = [5,4,3,2,1]
quick_sort(arr,0,len(arr)-1)
print(arr)

# Time Complexity -- O(n*log n)
# Space Complexity -- O(n)






    
