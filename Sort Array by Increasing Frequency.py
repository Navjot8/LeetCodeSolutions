from itertools import repeat

nums = [1, 1, 2, 2, 2, 3]
nums = [2, 3, 1, 3, 2]
nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
temp = []
t = []
k = []
nums=sorted(nums,reverse=True)
print(nums)
dictionaryofnums = {i: nums.count(i) for i in nums}
dictionaryofnums = dict(sorted(dictionaryofnums.items(), key=lambda a: (a[1], a[0])))

lis = [key for key, val in dictionaryofnums.items() for i in range(val)]
firstVal = list(dictionaryofnums.items())[0][1]
print(sorted(lis))

# dictionaryofnums[9000] = 10000

# for key, val in dictionaryofnums.items():
#     b = val
#     if val != firstVal:
#         firstVal = val
#         temp.append(sorted(t)[::-1])
#         t = []
#         t.extend(repeat(key, val))
#     else:
#         t.extend(repeat(key, val))
#
# for i in temp:
#     k += i
# print(k)
