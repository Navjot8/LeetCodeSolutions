class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # words = ["cool","lock","cook"]
        j=1
        l1=[]
        for i in words[0]:
            j=1
            count=1
            while j<len(words):
                if i in words[j]:
                    t=list(words[j])
                    t.remove(i)
                    words[j]="".join(t)
                    count+=1
                if count==len(words):
                    l1.append(i)
                j+=1
        return (l1)

