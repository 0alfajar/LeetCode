class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        sum_nums = []
        for num in nums:
            num = str(num)
            sum_digit = 0
            for digit in num:
                sum_digit += int(digit)
            sum_nums.append(sum_digit)
            
        for i in range(len(sum_nums)):
            if i == sum_nums[i]:
                return i    
        return -1