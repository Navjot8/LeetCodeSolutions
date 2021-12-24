class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        l=[]
        for i in image:
            l.append(i[::-1])
        l1=[]
        for i in l:
            t=[]
            for k in i:
                if k==1:
                    t.append(0)
                else:
                    t.append(1)
            l1.append(t)
        return l1