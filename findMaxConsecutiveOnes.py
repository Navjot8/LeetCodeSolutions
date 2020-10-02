class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0;
        max = 0;
        nums += [0];
        for i in range(0, len(nums)):
            if (nums[i] == 0):
                if (max < count):
                    max = count;
                count = 0;
            else:
                count += 1;

        return max;
