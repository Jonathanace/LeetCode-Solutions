class Solution:
    def convert(self, s: str, n: int) -> str:
        res = [[] for _ in range(n)]
        # print(res)
        i = 0
        l = len(s)
        while i < l:
            j = 0
            while j < n and (i + j) < l: # doing down
                res[j].append(s[i + j])
                j += 1
                
            # print(res)

            i += j
            j = 0
            while j < n-2 and (i + j) < l: # going up
                res[-(j+2)].append(s[i+j])
                j += 1
            
            i += j
            
        return ''.join([''.join(i) for i in res])