class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cost = prices[0]
        for revenue in prices[1:]:
            profit = max(profit, revenue - cost)
            cost = min(cost, revenue)
        
        return profit