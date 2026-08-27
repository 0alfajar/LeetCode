class Solution:
    def countKeyChanges(self, s: str) -> int:
        shift = 0
        for i in range(len(s)-1):
            if s[i].lower() != s[i+1].lower():
                shift += 1
        return shift
