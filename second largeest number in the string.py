class Solution:
    def secondHighest(self, s: str) -> int:
        numbers="0123456789"
        newNumber=""
        max=-1
        t=""
        for i in s:
            if i in numbers:
                t+=i
                if i not in newNumber:

                    newNumber=i
                    if int(newNumber)>max:
                        max=int(newNumber)
        secondMax=-1
        for i in set(t):
            if int(i)!=max:
                if int(i)>secondMax:
                    secondMax=int(i)
        return (secondMax)