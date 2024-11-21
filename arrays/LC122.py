class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Base Case:
        if len(prices) == 1:
            return 0

        i = 0
        profit = 0
        bought = -1
        while i < len(prices)-1:
            if prices[i] < prices[i+1]:
                bought = prices[i]
                while i < len(prices)-1 and prices[i+1] > prices[i]:
                    i += 1
                if prices[i] != bought:
                    profit += prices[i] - bought
            i += 1

        if profit == 0:
            if prices[-1] > prices[0]:
                return prices[-1] - prices[0]
            else:
                return 0

        return profit
        
'''
RT: O(n)
Space: O(1)

Identified the key idea, local minima and maxima, early, straight forward solving from there

Less lines of code, but less clear, discussion board solution

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0 or len(prices)==1:
            return 0
        max_profit = 0
        right = 1
        while right < len(prices):
            if prices[right] > prices[right-1]:
                max_profit += prices[right] - prices[right-1]
            right += 1
        return max_profit
        
'''