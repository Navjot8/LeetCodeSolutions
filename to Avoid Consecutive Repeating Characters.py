import random
s = "??yw?ipkj?"
s="a?k"
s="?s??"
s="j?qg??b"
s="a?m"
s="ubv?w"
s="j?qg??b"
s="j?qg??b"
s="i??"
flag = False
alphabets = "abcdefghijklmnopqrstuvwxyz"
newlist=list(s)
start=0
end=25
for i in range(0,len(s)):
    if newlist[i]=="?":
        if i!= len(s)-1:
            print("inside")
            start=alphabets.find(newlist[i-1])+1
            if s[i+1]!="?":
                end=alphabets.find(newlist[i+1])-1
                if end<=start or end==start-1:
                    start=0
                    end=25
            else:
                 start=0
            newlist[i] = alphabets[random.randint(start, end)]
        else:
            start=alphabets.find(s[i-1])+1
            newlist[i]=alphabets[random.randint(start,25)]
print(newlist)


