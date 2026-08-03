class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        sub_nums = [nums[i:j] for i in range(n) for j in range(i + 1, n + 1)]
        sub_nums_distinct = [list(set(sub_num)) for sub_num in sub_nums]
        
        sum_square = 0
        for sub_num_distinct in sub_nums_distinct:
            sum_square += len(sub_num_distinct)**2
        
        return sum_square
            