class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l=[]
        for i in range(0,len(nums)):
            for k in range(i+1,len(nums)):
                if nums[i]==nums[k] and i<k:
                    l.append([i,k])
        return len(l)