class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        nums = []
        for c in s:
            if c.isdigit():
                nums.append(int(c))
        
        asc = True
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                asc = False
                break
            else:
                asc = True
        
        return asc
