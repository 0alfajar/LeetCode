class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer1 = []
        for num in nums1:
            if num not in nums2:
                answer1.append(num)
        
        answer2 = []
        for num in nums2:
            if num not in nums1:
                answer2.append(num)

        answer1 = list(set(answer1))
        answer2 = list(set(answer2))
        
        return [answer1, answer2]
