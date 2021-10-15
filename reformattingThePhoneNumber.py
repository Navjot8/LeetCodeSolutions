class Solution:
    def reformatNumber(self, number: str) -> str:
        newNumber = ""
        for i in number:
            if i != " " and i != "-":
                newNumber += i
        count = 0
        i = 0
        t = ""
        finalNumber = ""
        while i < len(newNumber):
            if count != 3:
                finalNumber += newNumber[i]
                t += newNumber[i]
            else:
                finalNumber += "-"
                count = -1
                i -= 1
            count += 1
            i += 1

        if finalNumber[-2:][0] == "-":
            k = newNumber[-4:]
            finalNumber = finalNumber[:-5] + k[:2] + "-" + k[2:]
        return (finalNumber)


