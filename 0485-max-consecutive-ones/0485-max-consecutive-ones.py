class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_ones = []
        count = 0
        for num in nums:
            if num == 0:
                consecutive_ones.append(count)
                count = 0
            else:
                count += 1
        consecutive_ones.append(count)
        return max(consecutive_ones)