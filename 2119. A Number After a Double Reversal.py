class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num = str(num)
        num1 = num[::-1]
        print(num1)
        count = 0
        for i in num1:
            if i == "0":
                count += 1
            else:
                break
        if count == len(num):
            return True

        return num1[count:][::-1] == num

