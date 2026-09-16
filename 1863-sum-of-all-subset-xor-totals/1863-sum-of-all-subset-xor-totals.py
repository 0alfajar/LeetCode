from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_sum = 0
        subset_arr = [list(c) for r in range(1, len(nums) + 1) for c in combinations(nums, r)]
        for arr in subset_arr:
            xor = 0
            for num in arr:
                xor ^= num
            xor_sum += xor
        return xor_sum

                

