class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)
        product=(nums[-2]-1)*(nums[-1]-1)
        return product