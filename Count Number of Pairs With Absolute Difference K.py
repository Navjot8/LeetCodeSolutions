nums = [1,2,2,1]
k = 1
count=0
for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        if abs(nums[i]-nums[j])==k:
            count+=1
