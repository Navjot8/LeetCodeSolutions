class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counterNumber = {}
        for i in nums:
            if i not in counterNumber:
                counterNumber[i] = 0
            counterNumber[i] += 1

        counter = 0
        temp = list(sorted(counterNumber.items(), key=lambda x: (x[0], x[1])))

        for i in range(len(temp) - 1):
            if abs(temp[i][0] - temp[i + 1][0]) == 1:
                if temp[i][1] + temp[i + 1][1] > counter:
                    counter = temp[i][1] + temp[i + 1][1]
        return (counter)