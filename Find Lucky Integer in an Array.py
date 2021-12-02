def matchString(txx,pattern):
    for i in range(len(txx)-len(pattern)+1):
        j=0
        while j<len(pattern):
            if txx[i+j]!=pattern[j]:
                break
            j+=1
        if j==len(pattern):
            print("latter found at index",i)
def binarySearch(numsber,arr):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+end//2
        if arr[mid]==numsber:
            return mid
        elif arr[mid]<numsber:
            start=mid+1
        else:
            end=mid-1
    return -1
print(binarySearch(4,[1,2,3,4]))
# matchString("jasndfnjnninisadfuuhuwehrhubaiunsdfjnackonasfnacoonsddonfnacnonninonsancancanac","nac")