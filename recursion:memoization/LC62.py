class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = {}
        def recurse(x, y):
            if(x == n - 1 and y == m - 1):
                return 1
            if(x > n or y > m):
                return 0
            if (x, y) in memo:
                return memo[(x,y)]
            memo[(x,y)] = recurse(x, y + 1) + recurse(x + 1, y)
            return memo[(x,y)]

        return recurse(0,0)