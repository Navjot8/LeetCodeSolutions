s = "abaaba"
# print(s[2:])
g=len(s)
count=2
counter=0
for i in range(0,len(s)//2):
    substring=s[:count]
    counter=count
    for k in range(count,len(s),count):
        r=s[k:k+count]
        if len(r)!=len(substring):
            print("False")
            break
        elif substring==s[k:k+count]:
            counter+=count
    if counter==len(s):
        print("true")
        break;
    count+=1
print("false")