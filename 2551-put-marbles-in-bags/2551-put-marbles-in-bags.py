class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:                        
        splits = sorted(sum(weights[i:i+2]) for i in range(len(weights) - 1))
        return sum(splits[len(splits) - k + 1:]) - sum(splits[:k - 1])
    