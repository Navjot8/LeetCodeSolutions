s="aaaaaaabc"
goal =  "aaaaaaacb"
i=0
l=[]
while i<len(s):
    if s[i]!=goal[i]:
        l.append(i)
    i+=1
newGoal=list(goal)
temp=newGoal[l[0]]
newGoal[l[0]]=newGoal[l[1]]
newGoal[l[1]]=temp
print(newGoal)