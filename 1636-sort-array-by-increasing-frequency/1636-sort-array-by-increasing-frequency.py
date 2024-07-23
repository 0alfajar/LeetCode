class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        m = Counter(nums)
        nums.sort(key=lambda x: (m[x], -x0)
        return nums