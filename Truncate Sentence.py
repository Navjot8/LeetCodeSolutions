class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # k = 4
        listOfs=s.split()
        i=0
        newSentence=""
        while i<k:
            newSentence+=listOfs[i]+" "
            i+=1
        return(newSentence[:-1])