s = "abacbc"
newString = ""
for i in s:
    if i not in newString:
        newString += i
l = [s.count(i) for i in newString]
print(l)
for i in range(len(l)-1):
    print(i)
    if l[i]!=l[i+1]:

        print("break")

