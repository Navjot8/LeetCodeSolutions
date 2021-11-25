class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # nums = [3, 1, 2, 4]
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        final = even + odd
        return (final)
