# import Counter
from collections import Counter

m=0
nums = [1,3,2,2,5,2,3,7]
counterNumber={}
for i in nums:
    if i not in counterNumber:
        counterNumber[i]=0
    counterNumber[i]+=1
print(counterNumber)
counter=0
temp=list(sorted(counterNumber.items(),key=lambda x:(x[0],x[1])))

for i in range(len(temp)-1):
    if abs(temp[i][0]-temp[i+1][0])==1:
        if temp[i][1]+temp[i+1][1]>counter:
            counter=temp[i][1]+temp[i+1][1]
print(counter)

