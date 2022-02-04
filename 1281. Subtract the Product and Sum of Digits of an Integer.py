class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sum1=0
        for i in str(n):
            sum1+=int(i)
            product*=int(i)
        return product - sum1