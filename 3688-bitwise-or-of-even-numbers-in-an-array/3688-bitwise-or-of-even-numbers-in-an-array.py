class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        even_nums = [num for num in nums if num%2==0]
        res = 0
        for num in even_nums:
            res |= num
        return res
