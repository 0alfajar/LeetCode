class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        while len(nums) > 0:
            averages.append(((min(nums) + max(nums)) / 2))
            nums.remove(max(nums))
            nums.remove(min(nums))
        return min(averages)