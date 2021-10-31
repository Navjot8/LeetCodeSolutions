class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = []
        l2 = []
        for i in s1.split():
            if i not in l1:
                l1.append(i)
        for i in s2.split():
            if i not in l1:
                l2.append(i)
        n1 = []
        n2 = []
        for i in l1:
            count = 0
            for k in s1.split():
                if i == k:
                    count += 1
            if count == 1:
                n1.append(i)

        for i in l2:
            count = 0
            for k in s2.split():
                if i == k:
                    count += 1
            if count == 1:
                n2.append(i)

        n3 = [j for j in n1 if j not in s2.split()]
        n4 = [k for k in n2 if k not in s1.split()]
        return (n3 + n4)
