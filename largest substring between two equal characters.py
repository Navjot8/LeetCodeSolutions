class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        flag=False
        maxlength=0
        for i in range(0,len(s)):
            for y in range(i+1,len(s)):
                if s[i]==s[y]:
                    k=s[i:y]
                    if len(k)>=maxlength:
                        maxlength=len(k)
        return (maxlength-1)