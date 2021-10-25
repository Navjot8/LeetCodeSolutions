class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        alpha="abcdefghijklmnopqrstuvwxyz*"
        word = word+"*"
        numbers=[]
        num=""
        i=0
        j=0
        flag=False
        while i< len(word):
            k=word[i]
            if word[i] not in alpha:
                j=i
                while word[j] not in alpha:
                    j+=1
                    flag=True
            t=word[i:j]
            if t!="":
                if int(t) not in numbers:
                    numbers.append(int(t))

            if flag:
                i=j
                flag=False
                i-=1
            i+=1
        return (len(set(numbers)))