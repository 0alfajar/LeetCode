class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        v = list(set(nums1)&set(nums2))
        if v:
            return min(v)
        else:
            return -1