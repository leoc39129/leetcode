class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Base Cases:
        if amount == 0:
            return 0
        
        # Does the greedy approach here work? Start with the highest value coin, use as
        # many of them as possible, once the remaining amount is smaller than that coin
        # use the smaller coins to see if you can satisfy the remaining amount?

        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for idx in range(1, len(dp)):
            poss = [dp[idx - value] + 1 for value in coins if idx - value >= 0 and dp[idx - value]!= -1]
            # print(poss)
            if len(poss) == 0:
                dp[idx] = -1
            else:
                dp[idx] = min(poss)

        return dp[amount]


'''
RT: O(amount*coins)
Space: O(amount)

I used a GPT hint, but this is an optimal solution using dp. Here's a similar discussion board solution

class Solution:
    def coinChange(self, coins, amount):
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])
        
        return min_coins[-1] if min_coins[-1] != amount + 1 else -1
'''