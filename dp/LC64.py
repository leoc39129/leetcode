class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)       # rows
        n = len(grid[0])    # cols

        if m == 1:
            return sum(grid[0])
        if n == 1:
            temp = 0
            for row in grid:
                temp += row[0]
        
        # Binary choice: You can only go down or right
        # dp = [[0]*n for _ in range(m)]
        # dp[0][0] = grid[0][0]

        for row in range(0, m):
            for col in range(0, n):
                if row == 0 and col == 0:
                    continue
                elif row == 0:
                    grid[row][col] = grid[row][col-1] + grid[row][col]
                elif col == 0:
                    grid[row][col] = grid[row-1][col] + grid[row][col]
                else:
                    grid[row][col] = min(grid[row][col-1], grid[row-1][col]) + grid[row][col]
        #print(dp)
        return grid[m-1][n-1]

        
'''
RT: O(n*m)
Space: O(1)

Straightforward problem, solved in ~15 mins. First solution used the commented code, made a 
whole new grid -- the runtime was the same, but the memory used was O(n*m). Good stuff seeing
that you can simply use the given grid, using O(1) space. Both solutions are O(n*m) RT.
'''