class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):

            if nums[i] == target:
                t = i
                l.append(i)
        if len(l) == 2:
            return l
        elif len(l) == 1:
            return [t, t]
        elif len(l) > 2:
            return [nums.index(target), nums.index(target) + (len(l) - 1)]
        else:
            return [-1, -1]
