class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum = sum([int(i) for i in str(n)])
        squareSum = sum([int(i)*int(i) for i in str(n)])

        return squareSum - digitSum >= 50