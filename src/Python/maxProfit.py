class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        price = prices[0]
        profit = 0

        for i in prices[1:]:
            if price > i: 
                price = i
            
            profit = max(profit, i - price)
        
        return profit
        