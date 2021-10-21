class Solution:
    def makeGood(self, s: str) -> str:
        newString = list(s)
        capalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        j = 1
        count = 0
        while count < 1290:
            count += 1
            try:
                if newString[i] in capalphabets and newString[j] in alphabets:
                    k = capalphabets.find(newString[i])
                    a = alphabets.find(newString[j])
                elif newString[i] in alphabets and newString[j] in capalphabets:
                    k = capalphabets.find(newString[j])
                    a = alphabets.find(newString[i])
                else:
                    k = 0
                    a = -1

                if (k == a):
                    newString[i] = ""
                    newString[j] = ""
                    temp = "".join(newString)
                    newString = list(temp)
                    i = 0
                    j = 1
                else:
                    i += 1
                    j += 1

            except:
                break
        return ("".join(newString))






 