import itertools

nums = [-1, 0, 1, 2, -1, -4]
print(sorted(nums))
dic = {}
nums = sorted(nums)
l = []
for i in set(itertools.combinations(nums,3)):
    if sum(i)==0:
        l.append(list(i))

# for i in range(len(nums)):
#     key = tuple(nums[i:3 + i])
#
#     if key not in dic.keys() and sum(nums[i:i + 3]) == 0:
#         dic[key] = [nums[i:i + 3]]
# print(dic)
