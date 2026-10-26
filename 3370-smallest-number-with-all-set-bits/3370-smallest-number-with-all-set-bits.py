class Solution:
    def smallestNumber(self, n: int) -> int:
        bit = bin(n)[2:]
        set_bit = ""
        for c in bit:
            set_bit += str(int(c) or 1)
        
        return int(set_bit, 2)


        