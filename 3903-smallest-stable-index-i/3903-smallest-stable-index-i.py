class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            largest = max(nums[:i+1])
            smallest = min(nums[i:])
            score = largest - smallest
            if score <= k:
                return i
        return -1
