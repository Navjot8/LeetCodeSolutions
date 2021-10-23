class Solution:
    def frequencySort(self, s: str) -> str:

        dic1 = {}
        newString = ""
        for i in s:
            if i not in newString:
                dic1[i] = s.count(i)
                newString += i
        finalString = ""
        t = (sorted(dic1.items(), key=lambda kv: (kv[1], kv[0])))
        t = t[::-1]
        for key, val in t:
            finalString += key * val
        return finalString