nums = [1,2,0,1]+[pow(2,31)]
nums = sorted(nums)
print(nums)
count = 1
maxcount = 0
for i in range(len(nums) - 1):
    if abs(nums[i] - nums[i + 1]) == 1:
        count += 1
    else:
        if count > maxcount:
            maxcount = count
            count = 1
print(maxcount)
