class OriginalDPSolution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2

        for idx in range(2, n):
            dp[idx] = dp[idx-2] + dp[idx-1]
        
        return dp[n-1]

# RT: O(n)
# Space: O(n)

# But we can do better ...


class OptimizedDPSolution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0]*3
        dp[0] = 1
        dp[1] = 2

        for idx in range(2, n):
            dp[2] = dp[1] + dp[0]
            dp[0] = dp[1]
            dp[1] = dp[2]
        
        return dp[2]


class SuperOptimizedDPSolution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        far = 1
        close = 2
        cur = 0

        for idx in range(2, n):
            cur = close + far
            far, close = close, cur
        
        return cur
        

'''
RT: O(n)
Space: O(1)

Easy to see solution!
'''
        
        