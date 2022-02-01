class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = [1,2,3,4,5,6,7]
        # k = 3
        for i in range(k):
            nums=nums[(len(nums)-1)-i:]+nums[:(len(nums)-1)-i]
        return (nums)