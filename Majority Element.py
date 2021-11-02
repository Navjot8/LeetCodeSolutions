class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums = [3,2,3]
        newNums=[]
        for i in nums:
            if i not in newNums:
                newNums.append(i)
        dic={}
        for i in newNums:
            dic[i]=nums.count(i)
        print(dic)
        # t = (sorted(dic1.items(), key=lambda kv: (kv[1], kv[0])))
        t=sorted(dic.items(), key=lambda k:(k[1],k[0]))
        return (t[::-1][0][0])