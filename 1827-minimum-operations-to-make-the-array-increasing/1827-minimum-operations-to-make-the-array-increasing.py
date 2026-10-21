class Solution:
    def minOperations(self, nums: List[int]) -> int:
        incr = 0
        for i in range(len(nums) - 1):
            if nums[i+1] <= nums[i]:
                incr += ((nums[i] + 1) - nums[i+1])
                nums[i+1] = nums[i] + 1
        return incr
