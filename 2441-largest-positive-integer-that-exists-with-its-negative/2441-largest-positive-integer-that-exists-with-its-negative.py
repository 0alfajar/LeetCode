class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_k = -1
        for num in nums:
            if num in nums:
                if (num * -1) in nums:
                    max_k = abs(num)
        return max_k