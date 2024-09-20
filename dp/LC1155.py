class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        if target < n:
            return 0
        
        # Initialize DP grid, rows are how many dice have been rolled, columns are total sum value of the dice so far
        # values in the grid are the number of ways to arrive at an outcome -- so look at the example in the block comment
        # below, (remember: DP[row][col]) DP[3][9] = 25 means there are 25 ways to roll a 9 with 3 standard 6 faced die 
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0] = 1

        MOD = 10**9 + 7

        # Here's the logic for the triple for loop...

        # 1. You have to fill in each row -- i.e. 0 dice rolled, 1 die rolled, ... and you have to do it top down
        #    it wouldn't make sense to go bottom up, as our base case here is 1 die rolled gets you one way to roll
        #    a 1, one way to roll a 2, ...

        # 2. For each die rolled, we have to fill in how many ways a certain target can be achieved
        #    with the given number of dice -- in other words, for each row, we have to fill in each column

        # 3. Here's the tricky part. Say for DP[2][9] -- what's the recursive relationship? In essence, you have to
        #    look at the previous row. The only way to know how many ways we can roll a 9 with two dice is to know
        #    where we can get with one die. So you look at the previous row where the target in the previous row 
        #    is less than the target in the current row -- because if we already rolled more than a 9 with one die, 
        #    there's no way we can get to 9 by adding a second die. The tricky part is knowing how far back to look
        #    in the table. In all...

        #    DP[2][9] = DP[1][3] + DP[1][4] + DP[1][5] + DP[1][6] + DP[1][7] + DP[1][8]

        #    How do we know that we don't have to look at DP[1][2] or DP[1][1]? We know this because you can't get from
        #    2 to 9 with a six faced die! Same goes for 1. If we had a seven faced die, we would need to add in DP[1][2].
        #    So, we look back 6 spots from 9, or the current target number minus the number of faces on the die, and sum
        #    all of those values up. However, sometimes we can't look that far back -- for example, think about DP[2][3].
        #    If we followed that rule blindly, we'd be looking at...

        #    DP[2][3] = DP[1][2] + DP[1][1] + DP[1][0] + DP[1][-1] + DP[1][-2] + DP[1][-3]

        #    so instead, we take the minimum of looking back k (or 6) spaces or the current target sum spaces back (in this case, 3)
        #    (also, the +1 is in the 3rd for loop because remember, range is EXCLUSIVE in python). That way, when we evaluate...

        #    DP[2][3] = DP[1][2] + DP[1][1] + DP[1][0] 
        
        for dice in range(1, n+1):
            for total_sum in range(1, target+1):
                for face in range(1, min(k+1, total_sum+1)):
                    dp[dice][total_sum] += dp[dice-1][total_sum-face] % MOD

        print(dp)
        print(dp[n][target])
        return dp[n][target] % MOD

        '''
        3 standard (6 faces) dice
        target: 11
        Horizontal: Total sum right now
        Vertical: How many dice are remaining

           0  1  2  3  4  5  6  7  8  9 10 11
       0  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       1  [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
       2  [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2]
       3  [0, 0, 0, 1, 3, 6,10,15,21,25,27,27]
        '''
        