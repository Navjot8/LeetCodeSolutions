class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if nums.count(i)==1:
                count+=i
        return count