class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Base Case:
        if len(triangle) == 1:
            return triangle[0][0]

        if len(triangle) == 2:
            return triangle[0][0] + min(triangle[1][0], triangle[1][1])

        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]

        for level in range(2, len(triangle)):
            triangle[level][0] += triangle[level-1][0]
            triangle[level][-1] += triangle[level-1][-1]
            for idx in range(1, len(triangle[level])-1):
                triangle[level][idx] += min(triangle[level-1][idx-1], triangle[level-1][idx])


        return min(triangle[len(triangle)-1])

'''
RT: O(n) - n being the size of the triangle, not the number of rows
Space: O(1)

A somewhat easy dynammic programming problem wow! If you're not allowed to modify the triangle itself...

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        memo = triangle[row-1].copy()

        for r in range(row-2, -1, -1):
            for c in range(r+1):
                memo[c] = min(memo[c], memo[c+1]) + triangle[r][c]
        
        return memo[0]
'''