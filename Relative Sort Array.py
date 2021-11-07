class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        dic = {}
        for i in arr2:
            dic[i] = arr1.count(i)
        newNums = []
        for key, val in dic.items():
            newNums.extend(repeat(key, val))
        t = []
        for i in arr1:
            if i not in newNums:
                t.append(i)
        return (newNums + sorted(t))
