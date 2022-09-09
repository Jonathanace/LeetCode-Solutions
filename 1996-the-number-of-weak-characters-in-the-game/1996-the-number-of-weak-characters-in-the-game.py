class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1])) # sorted by descending attack, ascending defense
        prev_max_defense = 0
        res = 0
        for attack, defense in properties: 
            if defense < prev_max_defense:
                res += 1 
            else:
                prev_max_defense = defense
        return res