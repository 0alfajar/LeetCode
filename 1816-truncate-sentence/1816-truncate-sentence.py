class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        text_split = s.split()

        res = text_split[0]

        for i in range(1, k):
            res += " " + text_split[i]
        
        return res