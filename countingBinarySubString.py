s = "01011100"

counter0=0
counter1=0
l=[]
i=0
finalString=""
while i<len(s):
    if s[i]=="0":
        counter0+=1
        if counter1==counter0:
            for k in range(1,counter1+1):
                l.append(k*"1"+k*"0")
            i-=counter1
            counter0=0
            counter1=0
        elif counter0<=counter1-1 and counter0>=2:
            for f in range(1,counter0+1):
                l.append("1"*f+"0"*f)
            i -= counter0
            counter0 = 0
            counter1 = 0
        elif counter1>1 and counter0==1 :
            l.append("10")
            i-=1
            counter1=0
            counter0=0
    elif s[i]=="1":
        counter1+=1
        if counter1==counter0:
            for j in range(1,counter0+1):
                l.append(j*"0"+j*"1")
            i-=counter0
            counter0=0
            counter1=0
        elif counter0>=counter1 and counter1>=2:
            for g in range(1,counter1+1):
                l.append("0"*g+"1"*g)
            i-=counter1
            counter0=0
            counter1=0
        elif counter0>1 and counter1==1 :
            l.append("01")
            i-=1
            counter1=0
            counter0=0
    i+=1
print(l)


