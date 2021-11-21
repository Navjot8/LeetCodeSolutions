from itertools import repeat

left = 47
right = 85

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        finalList = []
        listnums = [i for i in range(left, right + 1)]
        for i in listnums:
            k = i
            count = 0
            while k != 0:
                m = k % 10
                if m!=0:
                    if i % m == 0:
                        count += 1
                    if count == len(str(i)):
                        finalList.append(i)
                    k //= 10
                else:
                    break
        return finalList

print(finalList)
