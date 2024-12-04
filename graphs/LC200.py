class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        islands = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    islands += 1
                    self.dfs(grid, row, col)

        return islands

    def dfs(self, grid, row, col):
        if grid[row][col] == "1":
            grid[row][col] = "2"

            m = len(grid)
            n = len(grid[0])

            if row-1 > -1:
                self.dfs(grid, row-1, col)
            if row+1 < m:
                self.dfs(grid, row+1, col)
            
            if col-1 > -1:
                self.dfs(grid, row, col-1)
            if col+1 < n:
                self.dfs(grid, row, col+1)



class OldSolution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """  

        def dfs(row, col):
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()
                if 0 <= row < rows and 0 <= col < cols:
                    if grid[row][col] == "1" and visited_grid[row][col] == 0:
                        visited_grid[row][col] = 1
                        stack.append((row - 1, col))
                        stack.append((row + 1, col))
                        stack.append((row, col - 1))
                        stack.append((row, col + 1))
          

        # This time let's add [row, col] to visited
        count = 0

        cols = len(grid[0])
        rows = len(grid)

        visited_grid = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                tup = (i, j)
                if grid[i][j] == "1":
                    if visited_grid[i][j] == 0:
                        count += 1
                        dfs(i, j)
        
        return count


'''
Graphs aren't always about nodes and edges! Traversing a grid and using BFS/DFS is just as much
a graph problem as some of the other problems in this directory.

Here's a BFS iterative solution, and a non nested version afterwards


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands


from collections import deque

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    self.bfs(r, c, grid, visited, rows, cols)

        return islands

    def bfs(self, r, c, grid, visited, rows, cols):
        """
        Perform BFS to mark all connected '1's as visited
        :type r: int
        :type c: int
        :type grid: List[List[str]]
        :type visited: set
        :type rows: int
        :type cols: int
        """
        q = deque()
        visited.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == "1" and
                    (nr, nc) not in visited
                ):
                    q.append((nr, nc))
                    visited.add((nr, nc))

'''