class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        alt_num = []
        for i in range(0,len(nums)):
            if i % 2 != 0:
                nums[i] = nums[i] * -1
                alt_num.append(nums[i])
            else:
                alt_num.append(nums[i])
            
        return sum(alt_num)

