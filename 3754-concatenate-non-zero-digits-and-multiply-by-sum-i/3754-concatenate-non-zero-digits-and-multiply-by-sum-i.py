class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            non_0_digits = [int(digit) for digit in str(n) if digit != "0"]
            return int("".join(map(str, non_0_digits))) * sum(non_0_digits)