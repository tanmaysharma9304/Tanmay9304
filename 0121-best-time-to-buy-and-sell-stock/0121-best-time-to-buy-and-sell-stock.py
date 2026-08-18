class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = prices[0]
        profit = 0

        for price in prices:
            if price < minimum:
                minimum = price

            if price - minimum > profit:
                profit = price - minimum

        return profit