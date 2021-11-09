nums = [0,1,0,3,12]
zeros=nums.count(0)
print(zeros)
count=0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[count]=nums[i]
        count+=1
for i in range(count,len(nums)):
    nums[i]=0
print(nums)