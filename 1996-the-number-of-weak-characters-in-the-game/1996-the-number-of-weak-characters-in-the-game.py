class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1])) # sorted by descending attack, ascending defense
        prev_def = 0
        res = 0
        for _, cur_def in properties: 
            if cur_def < prev_def:
                res += 1 
            else:
                prev_def = cur_def
        return res