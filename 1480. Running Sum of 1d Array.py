nums = [1,2,3,4]
l=[]
for i in range(1,len(nums)+1):
    l.append(sum(nums[:i]))
