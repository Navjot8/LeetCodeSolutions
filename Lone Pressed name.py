def myCount(name):
    i=0
    l=[]
    t=0
    counter=0
    while(i<len(name)-1):
        # print(i)
        if name[i]==name[t]:
            counter+=1
            t+=1
        else:
            l.append(counter)
            counter=0
            i=t
    return l
"xnhtq"
"xhhttqq"
name ="a"+"*"
typed = "b"+"*"
l1=myCount(name)
l2=myCount(typed)
print(l1,l2)
flag=False
for i in range(0,len(l1)):
    if l1[i]<=l2[i]:
        flag=False
    else:
        flag=True
        break
if flag:
    print("False")
else:
    print("True")