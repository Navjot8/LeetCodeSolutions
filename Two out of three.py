class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        newNums = nums1 + nums3 + nums2
        nums = []
        for i in newNums:
            count = 0
            if i in nums1:
                count += 1
            if i in nums2:
                count += 1
            if i in nums3:
                count += 1
            if count > 1:
                nums.append(i)
        return (set(nums))