class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: 
            return 0

        best = 0
        low = float('inf')
        
        for i in prices:
            low = min(low, i)
            print(low)
            best = max(best, i-low)
        
        return best
