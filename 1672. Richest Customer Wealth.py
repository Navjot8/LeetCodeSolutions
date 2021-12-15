class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum=0
        for i in accounts:
            s1=sum(i)
            if s1>maximum:
                maximum=s1
        return maximum