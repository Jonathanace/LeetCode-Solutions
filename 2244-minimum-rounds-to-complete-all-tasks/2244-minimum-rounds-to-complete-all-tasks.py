class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        d = {2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3}
        def count(n):
            if n == 1:
                return False
            elif n not in d:
                d[n] = 1 + min(count(n-2), count(n-3))
            return d[n]
        
        freqs = {}
        for task in tasks:
            freqs[task] = freqs.get(task, 0) + 1
        
        res = 0
        for task in set(tasks):
            cur = count(freqs[task])
            if not cur:
                return -1
            res += count(freqs[task])
            
        return res