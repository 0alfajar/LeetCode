class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        
        for i in range(n):
            current_sum = 0
            for ii in range(i, n):
                current_sum += nums[ii]
                subarray_sums.append(current_sum)

        sorted(subarray_sums)
        
        mod = (10**9) + 7
        
        return sum(subarray_sums[left-1:right]) % mod

