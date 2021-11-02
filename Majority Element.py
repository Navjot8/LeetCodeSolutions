nums = [3,2,3]
newNums=[]
for i in nums:
    if i not in newNums:
        newNums.append(i)
dic={}
for i in newNums:
    dic[i]=nums.count(i)
print(dic)