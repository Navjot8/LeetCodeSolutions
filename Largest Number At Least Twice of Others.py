def dominantIndex(self, nums: List[int]) -> int:
    max1 = sorted(nums)[-1]
    count = 0
    if len(nums) == 1:
        return 0
    for i in sorted(nums):
        if i * 2 <= max1 and i != max1:
            count += 1
        else:
            break

    if count == len(nums) - 1:
        return nums.index(max1)
    else:
        return -1
