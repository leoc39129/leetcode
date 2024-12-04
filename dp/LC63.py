class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                # OOB
                # Obstacles
                if obstacleGrid[row][col] == 0:
                    if row > 0 and obstacleGrid[row-1][col] == 0:
                        dp[row][col] += dp[row-1][col]

                    if col > 0 and obstacleGrid[row][col-1] == 0:
                        dp[row][col] += dp[row][col-1]
                  
        return dp[m-1][n-1]
        

'''
RT: O(n*m)
Space: O(n*m)

Needed the hint but I got it in optimal RT and space complexity. Originally I was thinking "forward",
as in from dp[row][col] populate dp[row+1][col] and dp[row][col+1]. Instead, I needed to be thinking 
"backward", looking at dp[row-1][col] and dp[row][col-1] from dp[row][col]. From there it was smooth sailing.

Here's a little trick I thought of to use obstacleGrid itself for O(1) space complexity
'''
class NegativeSolution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        obstacleGrid[0][0] = -1

        for row in range(m):
            for col in range(n):
                # OOB
                # Obstacles
                if obstacleGrid[row][col] == 0:
                    if row > 0 and obstacleGrid[row-1][col] != 1:
                        obstacleGrid[row][col] += obstacleGrid[row-1][col]

                    if col > 0 and obstacleGrid[row][col-1] != 1:
                        obstacleGrid[row][col] += obstacleGrid[row][col-1]
                  
        return -1*obstacleGrid[m-1][n-1]


# and here's my solution from way back in March 2023... ew

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
