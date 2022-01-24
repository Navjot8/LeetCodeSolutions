class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l = title.split()
        t = []
        for i in l:
            if len(i) > 2:
                k = i.lower()
                t.append(k[0].upper() + k[1:])
            else:
                t.append(i.lower())
        return " ".join(t)
