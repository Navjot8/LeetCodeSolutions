class Solution:
    def findComplement(self, num: int) -> int:

        number = "{0:0b}".format(num)
        newB = ""
        for i in number:
            if i == "0":
                newB += "1"
            else:
                newB += "0"
        return int(newB, 2)

