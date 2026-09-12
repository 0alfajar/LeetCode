class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1, 2):
                res.append(sum(arr[i:j]))
        return sum(res)