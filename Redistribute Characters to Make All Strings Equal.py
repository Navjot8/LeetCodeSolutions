class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # words = ["abc","aabc","bc"]
        dic = {}
        for i in "".join(words):
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        for key, val in dic.items():
            if val % len(words) != 0:
                return False
        return True
