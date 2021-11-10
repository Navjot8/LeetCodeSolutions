s1 = "qgqeg"
s2="gqgeq"

dic1 = {}
for i in s1:
    if s1.count(i) != s2.count(i):
        print("False")
dic1={}
for i in s1:
    if i not in dic1:
        dic1[i]=s1.find(i)
print(dic1)
dic2={}
for i in s2:
    if i not in dic2:
        dic2[i]=s2.find(i)
print(dic2)
count=0
for key,val in dic2.items():
    val1=dic1[key]
    if val1!=val:
        count+=1

if count<3:
    print("true")
else:
    print("False")