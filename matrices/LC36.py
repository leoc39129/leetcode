class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for row in board:
            if not self.checkRow(row):
                return False

        for idx in range(len(board)):
            if not self.checkCol([row[idx] for row in board]):
                return False
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
                if not self.checkSquare(square):
                    return False
        
        return True
    
    def checkRow(self, row):
        seen = set()
        for token in row:
            if token != "." and token in seen:
                return False
            else:
                seen.add(token)

        return True


    def checkCol(self, col):
        # print(col)
        seen = set()
        for token in col:
            if token != "." and token in seen:
                return False
            else:
                seen.add(token)

        return True
    
    def checkSquare(self, square):
        seen = set()
        for token in square:
            if token != "." and token in seen:
                return False
            else:
                seen.add(token)


        return True


'''
Close but no cigar. Didn't index into columns and squares properly. Here's a simpler solution

class Solution:
    def isValidSudoku(self, board):
        # Initialize sets for rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                # Get the current cell value
                val = board[r][c]
                
                # Skip empty cells
                if val == '.':
                    continue
                
                # Calculate the index for the sub-box
                box_index = (r // 3) * 3 + (c // 3)
                
                # Check for duplicates in row, column, or sub-box
                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False
                
                # Add the value to the corresponding row, column, and sub-box
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        
        # If no duplicates were found, the board is valid
        return True

'''