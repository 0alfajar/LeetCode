class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missings = []

        for num in range(min(nums), max(nums)+1):
            if num not in nums:
                missings.append(num)
        
        return missings