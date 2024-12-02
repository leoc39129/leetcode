from collections import defaultdict

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Base Case:
        n = len(board)
        m = len(board[0])
        if n < 2 or m < 2:
            return

        graph = defaultdict(list)
        
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'X':
                    continue
                graph[(row, col)] = []
                if row < n-1:
                    if board[row+1][col] == 'O':
                        graph[(row, col)].append((row+1, col))
                if row > 0:
                    if board[row-1][col] == 'O':
                        graph[(row, col)].append((row-1, col))
                if col < m-1:
                    if board[row][col+1] == 'O':
                        graph[(row, col)].append((row, col+1))
                if col > 0:
                    if board[row][col-1] == 'O':
                        graph[(row, col)].append((row, col-1))

        visited = set()
        for key in graph:
            if key in visited:
                continue
            visited.add(key)
            surrounded = True
             
            trav = [key]
            region = set()

            while trav:
                node = trav.pop()

                if node not in visited:
                    visited.add(node)

                region.add(node)

                if node[0] == 0 or node[0] == n-1 or node[1] == 0 or node[1] == m-1:
                    surrounded = False
                for neighbor in graph[node]:
                    if neighbor not in region:
                        trav.append(neighbor)
            if surrounded:
                region = list(region)
                for key in region:
                    board[key[0]][key[1]] = 'X'


'''
RT: O(nm)
Space: O(nm)

This solution could be optimized a LOT. But...

This isn't really a graph problem, but I want the practice so I solved it that way. Here's a much
simpler solution, with the same complexity (instead of a queue, you could also use recursive dfs):

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([])

        for r in range(m):
            if board[r][0] == "O":
                queue.append((r, 0))
                board[r][0] = "#"
            if board[r][n - 1] == "O":
                queue.append((r, n - 1))
                board[r][n - 1] = "#"
        
        for c in range(1, n - 1):
            if board[0][c] == "O":
                queue.append((0, c))
                board[0][c] = "#"
            if board[m - 1][c] == "O":
                queue.append((m - 1, c)) 
                board[m - 1][c] = "#"
        
        while queue: 
            row, col = queue.popleft()

            for ro, co in dirs: 
                nr, nc = row + ro, col + co 
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    queue.append((nr, nc))
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
'''