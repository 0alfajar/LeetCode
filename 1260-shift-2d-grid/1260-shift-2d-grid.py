import numpy as np
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        np_grid = np.array(grid)
        shifted_grid = np.roll(np_grid, shift=k)
        return shifted_grid.tolist()
        
