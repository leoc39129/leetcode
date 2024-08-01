class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid[0]) - 1
        m = len(obstacleGrid) - 1
        
        # If top left or bottom right corner has the obstacle, there are no paths
        if obstacleGrid[0][0] == 1 or obstacleGrid[m][n] == 1:
            return 0
        
        memo = [[-1 * obstacleGrid[k][i] for i in range(len(obstacleGrid[0]))] for k in range(len(obstacleGrid))]
        # Use -1 to represent obstacles

        def recurse(x, y):
            # Corner Check
            if(x == n and y == m):
                return 1

            # Out of bounds check
            if(x > n or y > m):
                return 0

            if memo[y][x] == -1:
                return 0
            if memo[y][x] != 0:
                return memo[y][x]

            memo[y][x] = recurse(x, y + 1) + recurse(x + 1, y)
            return memo[y][x]

        return recurse(0,0)