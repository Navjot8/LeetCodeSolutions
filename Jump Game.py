nums =[0]
index=0
sum=0
length=len(nums)
while length>=0:
    try:
        length-=nums[index]
        index+=nums[index]
        if nums[index]==0:
            break
    except:
        break
    # index=0
print(length)
if length<=1:
    print("True")
else:
    print("False")


