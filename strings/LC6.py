class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Base Case:
        if len(s) == 1:
            return s

        cols = 0
        idx = 0
        ch = 0
        while ch < len(s):
            # print(idx)
            # print(ch)
            if (idx+1) % numRows == 0:
                cols = cols + numRows - 1
                idx = 0
                ch += numRows - 1
            else:
                idx += 1
                ch += 1

        if idx != 0:
            cols += 1

        print(cols)
        print(idx)


        matrix = [[0]*cols for _ in range(numRows)]
        print(matrix)
        

'''
Good ideas, horrible execution. Spent a lot of time trying to just iterate the string,
which won't work. Almost set up the matrix with the correct number of columns, and from
there it would've been easy. 

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Base Case:
        if len(s) == 1 or numRows == 1:
            return s
        
        idx = 0
        cols = 0
        skip = numRows+numRows-2

        # For each column and diagonal, add the correct number of columns
        for i in range(0, len(s), skip):
            idx = i
            if len(s) - i < skip:
                break
            cols += 1 + numRows-2

        # There might be some characters leftover, add the appropriate
        # number of columns if so
        if idx < len(s):
            cols += 1
            idx += numRows
        while idx < len(s):
            cols += 1
            idx += 1
        

        matrix = [[0]*cols for _ in range(numRows)]
        row, col = 0, 0

        idx = 0
        while idx < len(s):
            if row+1 == numRows:
                # Fill in the matrix diagonal with the right letters!
                matrix[row][col] = s[idx]
                idx += 1
                while row != 0 and idx < len(s):
                    row -= 1
                    col += 1
                    # print(str(row) + ", " + str(col))
                    matrix[row][col] = s[idx]
                    idx += 1
            elif row == 0 and col != 0:
                row += 1     
            else:
                matrix[row][col] = s[idx]
                idx += 1
                row += 1

        row, col = 0, 0
        lst = []
        while row < numRows:
            if matrix[row][col] != 0:
                lst.append(matrix[row][col])
            col += 1
            if col == cols:
                row += 1
                col = 0

        return ''.join(lst)

        
Got this to pass all test cases, and RT: O(n). Super slow code nevertheless, and space is O(n).

Here's a discussion board solution:

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)   
        
'''