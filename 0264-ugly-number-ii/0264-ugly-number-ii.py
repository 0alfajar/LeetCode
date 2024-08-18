class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0

        while len(ugly) < n:
            next_ugly = min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
            ugly.append(next_ugly)
            if ugly[i2] == ugly[i2] * 2:
                ugly[i2] += 1
            if ugly[i3] == ugly[i3] * 3:
                ugly[i3] += 1
            if ugly[i5] == ugly[i5] * 5:
                ugly[i5] += 1
                
        return ugly[-1]
