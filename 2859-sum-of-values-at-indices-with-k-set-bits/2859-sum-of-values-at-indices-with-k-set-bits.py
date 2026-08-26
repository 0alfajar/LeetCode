class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        bit_of_idx = [bin(i)[2:] for i in range(len(nums))]
        ones_digits_only = [bit.replace("0", "") for bit in bit_of_idx]

        result = 0
        for i in range(len(nums)):
            if len(ones_digits_only[i]) == k:
                result += nums[i]

        return result

