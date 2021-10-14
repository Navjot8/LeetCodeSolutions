class Solution:
    def reformat(self, s: str) -> str:
        numbers = "1234567890"
        alphabets = "abcdefdhijklmnopqrstuvwxyz"
        num = ""
        alpha = ""
        finalString = ""
        count = 0
        countfornumbers = 0
        if s.isalpha() and len(s) > 1:
            return ""
        elif s.isnumeric() and len(s) > 1:
            return ""
        else:
            for i in s:
                if i in numbers:
                    num += i
                else:
                    alpha += i
            if len(alpha) == len(num) + 1:
                for j in alpha:
                    finalString += j
                    if countfornumbers < len(num):
                        finalString += num[countfornumbers]
                        countfornumbers += 1

            elif len(alpha) <= len(num):
                for i in num:
                    finalString += i
                    if count < len(alpha):
                        finalString += alpha[count]
                        count += 1
            else:
                return ""
        return (finalString)



