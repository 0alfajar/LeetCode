class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort(reverse = True)

        sum = 0
        for i in range(len(grid[0])):
            maxVal = 0
            for j in range(len(grid)):
                maxVal = max(grid[j][i], maxVal)
            sum += maxVal

        return sum 
