class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        sum_of_digits = [sum(map(int, str(num))) for num in nums]
        idx = []
        for i in range(len(nums)):
            if i == sum_of_digits[i]:
                idx.append(i)
        if len(idx) > 0:
            return min(idx)
        else:
            return -1

