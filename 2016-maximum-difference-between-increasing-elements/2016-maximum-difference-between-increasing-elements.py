class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        for i in range(len(nums)):
            for j in range(len(nums)): 
                diff = abs(nums[i]-nums[j])
                if diff > max_diff and nums[i] < nums[j] and i < j:
                    max_diff = diff
        return max_diff
