# digits = "234"
# numberDic={"1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
# l=[]
# for i in digits:
#     l.append(list(numberDic[i]))
# print(l)
# count=0
# temp=l[0]
# b=[]
# # for i in range(0)

nums = [1,1,2]
newNums=['_']*len(nums)
temp=list(set(nums))
for i in range(0,len(temp)):
    newNums[i]=temp[i]
print(newNums)
