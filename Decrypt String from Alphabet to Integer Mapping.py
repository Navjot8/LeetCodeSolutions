class Solution:
    def freqAlphabets(self, s: str) -> str:
        decode=""
        alphabets="*abcdefghijklmnopqrstuvwxyz"
        decode=""
        c=s
        last=""
        flag=False
        if s[len(s)-1]!="#":
            flag=True
            j=s[len(s)-s[::-1].find("#"):]
            for h in j:
                last+=alphabets[int(h)]


        for i in range(0,s.count("#")):
            temp = c[:c.find("#")]
            find=temp
            if len(str(find))>2:
                d=find[:len(find)-2]
                for k in d:
                    decode+=alphabets[int(k)]
                decode+=alphabets[int(find[len(find)-2:])]
            else:
                decode+=alphabets[int(find)]
            try:
                c=c[c.find("#")+1:]

            except:
                break
        decode+=last
        return (decode)
