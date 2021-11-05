class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = "cat"
        # t = "rat"
        if len(s)==len(t):
            for i in t:
                if t.count(i)!=s.count(i):
                    return False
            return True
        return False