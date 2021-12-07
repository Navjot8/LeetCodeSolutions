class Solution:
    def reorderSpaces(self, text: str) -> str:
        # text ="a"
        numberOfSpaces = text.count(" ")
        t = text.split()
        newString = ""
        if len(t) == 1:
            newString += t[0] + numberOfSpaces * " "
        else:
            length = numberOfSpaces // (len(text.split()) - 1)
            for i in range(0, len(t) - 1):
                newString += t[i] + length * " "
            newString += t[len(t) - 1]
            remainingSpaces = numberOfSpaces % (len(text.split()) - 1)
            newString += remainingSpaces * " "
        return (newString)
