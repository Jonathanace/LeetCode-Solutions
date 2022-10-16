import functools
class Solution: # source: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/490316/JavaC%2B%2BPython3-DP-O(nd)-Solution
    def minDifficulty(self, A, d):
        n = len(A)
        if n < d: return -1

        @functools.lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(A[i:])
            res, maxd = float('inf'), 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, A[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res
        return dfs(0, d)