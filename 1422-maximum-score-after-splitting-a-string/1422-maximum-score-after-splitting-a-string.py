class Solution:
    def maxScore(self, s: str) -> int:
        score = []
        for i in range(1,len(s)):
            left = s[:i]
            right = s[i:]
            left_int = [int(item) for item in left]
            right_int = [int(item) for item in right]
            score.append((left_int.count(0) + right_int.count(1)))
        return max(score)