class Solution:
    def minElement(self, nums: List[int]) -> int:
        sum_of_digits = []
        for num in nums:
            sum_of_digits.append(sum([int(digit) for digit in str(num)]))
        return min(sum_of_digits)
