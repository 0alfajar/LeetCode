class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        left = 0
        right = sum(nums)

        for num in nums:
            left += num
            answer.append(abs(left - right))
            right -= num
        
        return answer
            