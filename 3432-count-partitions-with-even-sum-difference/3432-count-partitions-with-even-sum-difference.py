class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        even_sum_diff = 0
        for i in range(1, len(nums)):
            p1 = nums[:i]
            p2 = nums[i:]
            if (sum(p1) - sum(p2)) % 2 == 0:
                even_sum_diff += 1
        return even_sum_diff
        