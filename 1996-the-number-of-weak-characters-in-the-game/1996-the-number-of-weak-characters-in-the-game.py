class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1])) # sorted by descending attack, ascending defense
        prev_def = 0
        res = 0
        for character in properties: 
            if character[1] < prev_def:
                res += 1 
            else:
                prev_def = character[1]
        return res