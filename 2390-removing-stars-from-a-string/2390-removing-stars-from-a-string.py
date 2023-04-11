class Solution:
    def removeStars(self, s: str) -> str:
        indices = []
        for i in range(len(s)):
            if s[i] == '*':
                indices.append(i)
        
        sub_factor = 0
        while indices:
            index = indices.pop(0)
            index -= sub_factor
            sub_factor += 2
            s = s[:index-1] + s[index+1:]
            
        return s