class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        # Not really any base case
        # What I'm thinking is decompose each larger matrix into as many 3x3 matrices
        # we need to solve the problem, iteraively solve it?

        def find_matrix_max(mat):
            '''
            Find the maximum value in a 3x3 matrix
            :type mat: List[List[int]]
            :rtype: int
            '''
            return max(mat[0][0],mat[0][1],mat[0][2],
                        mat[1][0],mat[1][1],mat[1][2],
                        mat[2][0],mat[2][1],mat[2][2])

        n = len(grid)
        ret = [[0]*(n-2) for _ in range(n-2)]

        # Make a (n-2)(n-2) 3x3 matrices, pass them into the find matrix max
        # function, set its result as the correct index in the ret grid
        for row in range(n-2):
            for col in range(n-2):
                temp_mat = [grid[row][col:col+3],
                            grid[row+1][col:col+3],
                            grid[row+2][col:col+3]]
                #print(temp_mat)
                ret[row][col] = find_matrix_max(temp_mat)

        #print(ret)
        return ret