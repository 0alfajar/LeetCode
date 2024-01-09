class Solution:
    def finalValueAfterOperations(self, op: List[str]) -> int:
        ans = 0
        for i in range(len(op)):
            if(op[i] == '++X' or op[i] == 'X++'):
                ans = ans + 1
            else:
                ans = ans - 1
        return ans
        