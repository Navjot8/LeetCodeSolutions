import random
class Solution:
    # two possibilites either a number is even (if even make it odd) else it is odd
    def generateTheString(self, n: int) -> str:
        count=1
        string=""
        alpha="abcdefghijklmnopqrstuvwxyz"
        if n%2==0:
            n-=1
            string+=alpha[24]*n
            string+=alpha[1]
        else:
            string+=alpha[11]*n
        return string


