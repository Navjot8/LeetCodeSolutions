s = "a1b2c3d4e"
s = "a1c1e1"
alpha = "abcdefghijklmnopqrstuvwxyz"
finalString=""
for i in range(0,len(s)):
    if s[i] not in alpha:
        t=alpha.find(s[i-1])
        finalString+=alpha[t+int(s[i])]
    else:
        finalString+=s[i]
print(finalString)
