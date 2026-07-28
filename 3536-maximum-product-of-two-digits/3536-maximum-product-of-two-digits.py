class Solution:
    def maxProduct(self, n: int) -> int:
        n_sort = sorted([int(d) for d in str(n)], reverse=True)
        return n_sort[0] * n_sort[1]