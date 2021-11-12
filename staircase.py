class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins=n
        count=0
        for i in range(1,n+1):
            coins-=i
            if coins<0:
                break
            count+=1
        return  count