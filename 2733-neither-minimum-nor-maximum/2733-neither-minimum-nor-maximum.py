class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)

        if len(nums) <= 2:
            return -1
        else:
            return nums_sorted[:3][1]