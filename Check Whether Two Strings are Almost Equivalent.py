from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        uniletter=set(word1+word2)
        dic1=Counter(word1)
        dic2=Counter(word2)
        for i in uniletter:
            if abs(dic1[i]-dic2[i])>3:
                return False
        return True