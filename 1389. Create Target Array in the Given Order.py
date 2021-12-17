nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
# nums = [1,2,3,4,0]
# index = [0,1,2,3,0]
nums = [1]
index = [0]
newarr = [0] * len(nums)
for i in range(0, len(nums)):
    if newarr[index[i]] == 0:

        newarr[index[i]] = nums[i]
    else:

        t = newarr[:index[i]]
        t1 = newarr[index[i]:]

        newarr = t + [nums[i]] + t1
length = len(newarr) - len(nums)

print(newarr[:len(newarr) - length])
