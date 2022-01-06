class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWord = 0
        flag = False
        for i in sentences:
            t = i.split()
            if len(t) > maxWord:
                maxWord = len(t)

        return maxWord