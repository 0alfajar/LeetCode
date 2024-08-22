class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)
        complement = int(~binary)
        return complement