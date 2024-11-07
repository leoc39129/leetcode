class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Base Case:
        if len(prices) == 1:
            return 0

        profit = 0
        min_price = 100000

        for price in prices:
            if price - min_price > profit:
                profit = price - min_price
            elif price < min_price:
                min_price = price

        return profit


'''
RT: O(n)
Space: O(1)

Great job through and through! Don't forget to brainstorm with your own examples to find out flaws.
'''