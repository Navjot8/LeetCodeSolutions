from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        word1 = Counter(words1)
        word2 = Counter(words2)
        # print(word1,word2)
        # w=sorted(word1.items(),key=lambda x:(x[1],x[0]))
        # print(w)
        count = 0
        for key, val in word1.items():
            if key in word2.keys() and val == 1 and word2[key] == 1:
                count += 1
        return (count)
