class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        alpha="abcdefghijklmnopqrstuvwxyz"
        numbers=[]
        for i in s.split():
            try:
                numbers.append(int(i))
            except:
                c=0
        for i in range(0,len(numbers)-1):
            if numbers[i]>=numbers[i+1]:
                return False
        return True