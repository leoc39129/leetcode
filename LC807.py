class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # For each position grid[r][c], find the maximum values in the position's
        # row and column. The smaller of those two will be the new value, then 
        # increment the total skyline increase by that smaller value
        # That means we only need to find the n rows max's and n cols max's

        # Make two dictionaries, storing row and col maxs
        n = len(grid[0])
    
        rows = {}
        for r in range(n):
            rows[r] = max(grid[r])
        
        cols = {}
        for c in range(n):
            temp = -1
            for row in range(n):
                if grid[row][c] > temp:
                    temp = grid[row][c]
            cols[c] = temp

        sky_inc = 0
        inc = 0
        for r in range(n):
            row_max = rows[r]
            for c in range(n):
                inc = min(row_max, cols[c]) - grid[r][c]
                sky_inc += inc

        return sky_inc

# RT Complexity: O(N^2)
# Space Complexity: O(N)

# Reviewing discussion board and editorial, O(N^2) is the best RT we can do
# could've made the code more readable and short by using arrays rather than
# dictionaries to store row and col maximums, but this is an optimal solution otherwise
