class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        cur = k
        while cur in nums:
            cur += k
        return cur