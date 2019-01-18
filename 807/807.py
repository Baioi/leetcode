class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        

        maxRow = list(map(max, grid))
        maxCol = list(map(max, (zip(*grid))))

        # import numpy as np
        # maxRow = np.max(grid, axis=1)
        # maxCol = np.max(grid, axis=0)

        n = len(grid)
        height = 0
        for i in range(n):
            for j in range(n):
                num = int(min(maxRow[i], maxCol[j]))
                if grid[i][j]< num:
                    height += num - grid[i][j]
        return height

