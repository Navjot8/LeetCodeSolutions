class Solution:
    def countSubstrings(self, s: str) -> int:
        finalstring = ""
        count=0
        text=s
        for i in range(len(text)):
            x = ""
            for j in text[i:]:
                x += j
                if x == x[::-1]:
                    count+=1
        return count