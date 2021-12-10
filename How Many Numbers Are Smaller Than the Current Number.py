nums = [8, 1, 2, 2, 3]
# nums=["n","a","v"]
# nums=["nav","navj","a"]
# nums = [6,5,4,8]
nums=[2,2,2,2]
# nums=[6,3,7,6,9]
o = nums
nums = sorted(nums)
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1):
#         if nums[j]>nums[j+1]:
#             nums[j],nums[j+1]=nums[j+1],nums[j]


d = {i: nums.count(i) for i in nums}
l = [0] * len(nums)
count = 0
for key, val in d.items():

    t = nums.index(key)
    if d[key] > 1:
        for k in range(val):
            l[t + k] = count
        count += val - 1
    else:
        l[t] = count
    count += 1
newNums = []

for i in range(len(nums)):
    newNums.append([nums[i], l[i]])

final = [0] * len(nums)
length = len(newNums)
print(o)
for i in range(length):
    print(newNums[i][0])
    t = o.index(newNums[i][0])
    p = newNums[i][1]
    if final[t] == 0:
        final[t] = p
    else:
        final[t + 1] = p
    print(final)
    o[t]="*"
    # newNums=newNums[i:]
print(newNums)
print(final)




































