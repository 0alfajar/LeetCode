class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing = []
        for num in range(min(nums), max(nums) + 1):
            if num not in nums:
                missing.append(num)
        return missing