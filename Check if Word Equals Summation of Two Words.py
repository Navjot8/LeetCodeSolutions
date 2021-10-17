class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        num1 = ""
        num2 = ""
        num3 = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in firstWord:
            num1 += str(alphabet.find(i))
        for i in secondWord:
            num2 += str(alphabet.find(i))
        for i in targetWord:
            num3 += str(alphabet.find(i))
        if int(num1) + int(num2) == int(num3):
            return True
        else:
            return False
