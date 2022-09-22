class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cost = float('inf')
        for revenue in prices:
            profit = max(profit, revenue - cost)
            cost = min(cost, revenue)
        
        return profit