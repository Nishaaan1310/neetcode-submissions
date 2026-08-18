class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_val = 0
        low_val = prices[0]
        for i in range(1, len(prices)):
            low_val = min(low_val, prices[i])
            val =  prices[i] - low_val
            if val > max_val:
                profit = val
                max_val = val
            
        return profit

            

        