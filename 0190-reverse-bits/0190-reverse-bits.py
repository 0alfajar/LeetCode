class Solution:
    def reverseBits(self, n: int) -> int:
        hasil = 0
        for i in range(32):
            bit = (n >> i) & 1
            hasil = hasil | (bit << (31 - i))
        return hasil