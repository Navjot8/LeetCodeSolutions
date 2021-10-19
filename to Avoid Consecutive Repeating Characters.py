import random
s = "?as?"
alphabets="abcdefghijklmnopqrstuvwxyz"
if s[len(s)-1]=="?" and len(s)>=1:
    s+=alphabets[random.randint(0,25)]
s=list(s)
for i in range(0,len(s)):
    if s[i]=="?" and i <(len(s)-1):
        t=alphabets.find(s[i+1])
        # print(random.randint(random.randint(i,i*25)%10,25))
        s[i]=alphabets[random.randint(random.randint(0,i*25)%10,25)]
finalString=""
for i in range(0,len(s)-1):
    finalString+=s[i]
print(finalString)

print(random.seed(9001))
print(random.randint(0,25))
print(random.seed(9001))