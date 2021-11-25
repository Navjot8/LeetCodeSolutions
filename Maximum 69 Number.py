class Solution:
    def maximum69Number (self, num: int) -> int:
        # num = 9996
        t = ""
        count = 0
        for i in str(num):
            count += 1
            if i != "9":
                t += "9"
                break
            else:
                t += i
        k = str(num)

        return int(t + str(k[count:]))