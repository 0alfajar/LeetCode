class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        tf_nums = []
        for num in nums:
            if num % 2 == 0:
                tf_nums.append(0)
            else:
                tf_nums.append(1)
        return sorted(tf_nums)
