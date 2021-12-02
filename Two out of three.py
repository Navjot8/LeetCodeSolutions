nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
# algorithm
# creat new list and concate all the lists
# loop through the new list
# if any lement comes more than once put into new list

newNums=nums3+nums1+nums2
nums=[]
for i in newNums:
    count=0
    if i in nums3:
        count+=1
    if i in nums2:
        count+=1
    if i in nums1:
        count+=1
    if count>1:
        nums.append(i)
print(set(nums)) #creat a set to remove the duplicate from the list
