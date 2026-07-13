class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        digits_array = [int(digit) for digit in str(n)]
        return sum(digits_array)