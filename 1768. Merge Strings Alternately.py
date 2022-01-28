class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length=0
        flag1=False
        flag2=False
        if len(word1)<=len(word2):
            length=len(word1)
            flag1=True
        else:
            length=len(word2)
            flag2=True
        t=""
        for i in range(length):
            t+=word1[i]+word2[i]
        if flag1:
            t+=word2[length:]
        if flag2:
            t+=word1[length:]
        return t
