class Solution:
    def minimumMoves(self, s: str) -> int:
        string=s
        i=0
        counter=0
        while i<len(string):
            if string[i]=="X":
                t=string[i:i+3]
                if "X" in t:
                    counter+=1
                i+=2
            i+=1
        return(counter)