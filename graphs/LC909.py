class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # Base Case:
        n = len(board)
        if n < 3:
            return 1

        # for row in range(n):
        #     print("Row: " + str(row))
        #     for col in range(n):
        #         print(self.boustTranslation(n, row, col))
        for i in range(n*n):
            row, col = self.rowColTranslation(n, i)
            print("Row: " + str(row) + ", Col: " + str(col))
        return n

    def boustTranslation(self, n, row, col):
        if row % 2 == 1:
            return (n-1)*((n-1)-row)+col+1+(n-row-1)
        else:
            return (n-1)*((n-1)-row)+((n-1)-col)+(n-row)

    def rowColTranslation(self, n, num):
        # Don't call this on 36
        row = (n-1) - (num // n)
        col = (n-1) - (num % n) - 1

        return row, col

        
'''
Got absolutely stumped by this one, not sure how this is a "medium" but fine.
The general idea I think is quite intuitive and simple, I definitely got caught
up in minutiae instead of focusing on the big picture. Obviously this is BFS,
basically following every single possible move from a given square that you can reach.

Here's LeetCode editorial's code, with a kind of long but digestible editorial link below:
https://leetcode.com/problems/snakes-and-ladders/editorial


from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        
        # Screw the grid, why not just use a list
        cells = [None] * (n**2 + 1)                 # cells goes from idx 0 to n**2, don't use idx 0
        label = 1
        columns = list(range(0, n))                 # you always have the right column number, reverse it after every row
        for row in range(n - 1, -1, -1):            # row n-1, row n-2 ... (so for n=6: row 5, row 4, ...)
            for column in columns:
                cells[label] = (row, column)
                label += 1
            columns.reverse()

        # Instead of a defaultdict(list)/robust graph structure, if dist[num] == -1, it means it hasn't been visited;
        # So, only add unvisited "nodes" to the queue, and keep track of minimum "moves" by replacing -1 with the first
        # instance of reaching that "node", as that first instance will be the lowest number of moves to get there

        dist = [-1] * (n * n + 1)
        q = deque([1])
        dist[1] = 0

        while q:
            curr = q.popleft()
            for roll in range(curr + 1, min(curr + 6, n**2) + 1):
                row, column = cells[roll]

                destination = (board[row][column] if board[row][column] != -1
                               else roll)

                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    q.append(destination)

        return dist[n * n]


and GPT's optimizations:


from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        
        def get_destination(label):
            row = (n - 1) - (label - 1) // n
            column = (label - 1) % n if (n - 1 - row) % 2 == 0 else n - 1 - (label - 1) % n
            return board[row][column] if board[row][column] != -1 else label

        dist = {1: 0}
        q = deque([1])

        while q:
            curr = q.popleft()
            for roll in range(curr + 1, min(curr + 6, n**2) + 1):
                destination = get_destination(roll)
                if destination not in dist:
                    dist[destination] = dist[curr] + 1
                    if destination == n * n:  # Early exit
                        return dist[destination]
                    q.append(destination)

        return -1

'''