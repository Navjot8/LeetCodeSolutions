s ="aaa"
print(len(s))
i=0
j=0
count=0
l=[]
while i<(len(s)-1):
    if s[i]==s[j]:
        count+=1
        j+=1
    else:
        if count>=3:
            l.append([i,j-1])
        count=0
        i=j
print(l)
