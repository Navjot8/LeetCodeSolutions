class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # s = "xyzzaz"
        l=[]
        for i in range(0,len(s)):
            if len(s[i:i+3])==3:
                l.append(s[i:i+3])
        newL=[]
        for i in l:
            t=set(i)
            if len(t)==3:
                newL.append(i)
        return len(newL)