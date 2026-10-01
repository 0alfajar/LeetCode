class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        res = ""
        for i in range(len(arr)):
            if i == 0:
                res += arr[i][::-1]
            else:
                res += " " + arr[i][::-1]
        return res
