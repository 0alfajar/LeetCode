class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        check_s = s + s
        if len(s) == len(goal):
            if goal in check_s:
                return True
            else:
                return False
        else:
            return False