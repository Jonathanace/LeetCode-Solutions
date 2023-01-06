class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        total = 0
        res = 0
        for cost in sorted(costs):
            total += cost
            if total > coins:
                return res
            res += 1
        return res