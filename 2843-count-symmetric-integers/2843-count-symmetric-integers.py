class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        num_symmetric = 0
        for num in range(low, high+1):
            num_str = str(num)
            if sum(int(digit) for digit in num_str[:len(num_str)//2]) == sum(int(digit) for digit in num_str[len(num_str)//2:]) and len(num_str) % 2 == 0:
                num_symmetric += 1
        return num_symmetric
