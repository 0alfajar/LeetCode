class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        idx = 1
        for c in s:
            result += (123 - ord(c)) * idx
            idx += 1
        return result