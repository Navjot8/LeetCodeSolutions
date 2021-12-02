def checkSum(arr,target):
    start=0
    arr=sorted(arr)
    end=len(arr)-1
    while start<end:
        if arr[start]+arr[end]==target:
            return True
        elif arr[start]+arr[end]<target:
            start+=1
        else:
            end-=1
    return False

nums=sorted([1,2,3,4,5,2,723,123])
print(checkSum(nums,10))