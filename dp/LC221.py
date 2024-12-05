class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])

        # Base Case
        if m == 1 or n == 1:
            for row in range(m):
                for col in range(n):
                    if matrix[row][col] == "1":
                        return 1
            return 0

        dp = [[0]*n for _ in range(m)]
        max_area = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "1":
                    dp[row][col] = 1
                    if row > 0 and col > 0:
                        # We can form a square
                        min_sq = min(dp[row-1][col], dp[row-1][col-1], dp[row][col-1])
                        if min_sq == 1:
                            dp[row][col] = 4
                        elif min_sq % 2 == 0:
                            sqrt = math.sqrt(min_sq-q)
                            dp[row][col] = sqrt*sqrt
                        
                    if dp[row][col] > max_area:
                        max_area = dp[row][col]

        return max_area

        
'''
On the right track, didn't execute.

Here's the LeetCode editorial solution

RT: O(nm)
Space: O(nm)

class Solution:
    def maximalSquare(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        maxsqlen = 0
        # for convenience, we add an extra all zero column and row
        # outside of the actual dp table, to simpify the transition
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = (
                        min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1])
                        + 1
                    )
                    maxsqlen = max(maxsqlen, dp[i][j])
        return maxsqlen * maxsqlen

Realizing that we only need a 2x2 square (dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1], dp[i][j]),
here's an optimized space solution

RT: O(nm)
Space: O(n)

class Solution:
    def maximalSquare(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        dp = [0] * (cols + 1)
        maxsqlen = 0
        prev = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(min(dp[j - 1], prev), dp[j]) + 1
                    maxsqlen = max(maxsqlen, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return maxsqlen * maxsqlen
'''