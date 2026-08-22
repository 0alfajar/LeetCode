class Solution:
    def checkDivisibility(self, n: int) -> bool:
        arr = [int(i) for i in str(n)]

        prod = 1
        sums = 0
        for num in arr:
            prod *= num
            sums += num

        return n%(prod + sums) == 0
        