class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        
        # Let's recurse 
        total_count = 0
        ln = len(cost)
        strt = 0
        strt_idx = 0

        if cost[1] <= cost[0]:
            strt = cost[1]
            strt_idx = 1
        else:
            strt = cost[0]
            strt_idx = 0

        def recurse(cost_a, idx, count): 
            # Goal: determine whether to jump 1 or 2
            # if we can jump to the end, do it
            if idx >= ln - 2:
                return cost_a[idx]
            if cost[idx + 2] <= cost[idx + 1]:
                count += recurse(cost, idx + 2, count)
                return count
            else:
                count += recurse(cost, idx + 1, count)
                return count
        
        if ln == 2:
            return strt
        elif ln == 3:
            return min(cost[0] + cost[2], cost[1])
        elif ln == 4:
            return min(cost[0] + cost[2], cost[1] + cost[3],
            cost[1] + cost[2])
        else:
            total_count = recurse(cost, strt_idx, strt)

        # Now we have only cases where cost gets fed into the
        # recursion fn when it has 4 entries including idx
        # We start at the minimum of the first two entries if the
        # array is at least 3 entries long
        return total_count
        """
        '''
        # Dynamic Programming
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
        '''
        n = len(cost)
        return self.helper(cost, n)
    def helper(self, cost, n):
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        return min(self.helper(cost, n - 1) + cost[n - 1], 
        self.helper(cost, n - 2) + cost[n - 2])

            
