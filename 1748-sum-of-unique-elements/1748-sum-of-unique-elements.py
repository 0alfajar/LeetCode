class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        unique = []
        for num in nums:
            if nums.count(num) == 1:
                unique.append(num)
        return sum(unique)

        