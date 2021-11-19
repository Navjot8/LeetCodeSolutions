def binarySort(arr, val)-> int:
    start=0
    end=len(arr)
    while start<end:
        mid=start+end//2
        if arr[mid]==val:
            return mid
        elif arr[mid]<val:
            start=mid-1
        else:
            end=mid+1
    return -1
print(binarySort([1,2,3,4,5,6],10))
