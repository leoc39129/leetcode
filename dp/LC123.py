class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        
        # Initialize DP table
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]
        
        # Base cases for day 0
        for k in range(3):
            dp[0][k][0] = 0  # No stock held, profit is 0
            dp[0][k][1] = -prices[0]  # Holding stock after buying on day 0
        
        # Fill DP table
        for i in range(1, n):
            for k in range(1, 3):  # At most 2 transactions
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        
        # Return the maximum profit with at most 2 transactions and no stock held
        return max(dp[n-1][1][0], dp[n-1][2][0])

'''
GPT's Code:
RT: O(n)
Space: O(n)

So this is 3D dynamic programming, if I get one of these I'm cooked.

Anyway, the basic idea is...

dp[i][k][j]
i: day index
k: transactions left (0,1,2)
j: stock holding state (0 no, 1 yes)

Base Cases:
On day 0...
If you're not holding stock, you haven't spent anything, dp[0][k][0] = 0
If you are holding stock, you've spent prices[0] so, dp[0][k][1] = -prices[0]

Transition Rules:
1. Not Holding Stock (j=0)
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])

Either we carried over the state of not holding stock (dp[i-1][k][0])
or we sold the stock today, adding its value to the profit (dp[i-1][k][1]+prices[i])

2. Holding Stock (j=1)
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

Either we carried over the state of holding stock (dp[i-1][k][1])
or we bought stock today, reducing profits by the price today (dp[i-1][k-1][0] - prices[i])

Lastly, you need to choose the max between the best two separate transactions and the single best
transaction { max(dp[n-1][1][0], dp[n-1][2][0]) }


You can also optimize from 3D to 2D, simply holding two 2D arrays. If you have the same 3D array as above,
realize you only need two "slices" -- for a given i, you need dp[i][0:2][0:1] and dp[i-1][0:2][0:1] (not python accurate -- just for visualizing)

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        
        # Initialize DP arrays for 2 transactions
        prev = [[0, -prices[0]] for _ in range(3)]
        curr = [[0, -prices[0]] for _ in range(3)]
        
        # Fill the DP table iteratively
        for price in prices:
            for k in range(1, 3):  # At most 2 transactions
                curr[k][0] = max(prev[k][0], prev[k][1] + price)
                curr[k][1] = max(prev[k][1], prev[k-1][0] - price)
            prev = [row[:] for row in curr]  # Update prev with the current day
        
        # Maximum profit with 0 stock in hand and 2 transactions
        return prev[2][0]



There are a bunch of other solutions including an O(n) time, O(1) space solution below (in C++)... 
see more solutions and explanations at the link

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/solutions/796990/c-worst-to-best-solution-explained-for-dummies-like-me


int maxProfit(vector<int>& prices) {
        if(!prices.size())
            return 0;
        int buy1    = INT_MAX;
        int profit1 = INT_MIN;
        int buy2    = INT_MAX;
        int profit2 = INT_MIN;
        for(int i = 0; i < prices.size(); i++){
            buy1    = min(buy1, prices[i]);
            profit1 = max(profit1, prices[i] - buy1);
            buy2    = min(buy2, prices[i] - profit1);
            profit2 = max(profit2, prices[i] - buy2);
        }
        return profit2;
    }
'''