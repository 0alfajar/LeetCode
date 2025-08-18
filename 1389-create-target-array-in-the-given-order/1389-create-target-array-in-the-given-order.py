class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            if nums[index[i]] not in target:
                target.insert(index[i], nums[i])
        return target
