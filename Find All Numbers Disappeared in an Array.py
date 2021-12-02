nums = [1,1]
newNums=[]
for i in range(1, len(nums)+1):
    if i not in nums:
        newNums.append(i)
print(newNums)