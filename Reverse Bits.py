class Solution:
    def reverseBits(self, n: int) -> int:
        string=str(n)
        string=string[::-1]
        return (int(string,2))