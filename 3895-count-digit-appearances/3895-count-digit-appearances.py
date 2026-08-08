class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for num in nums:
            for c in str(num):
                if c == str(digit):
                    count += 1
        return count
