
class Solution:
    def equationsPossible(self, equations):
        union = {}
        def find(x): 
            if x not in union: 
                return x
            else:
                return find(union[x])
        
        # first pass, create union
        for equation in equations:
            a, b, operator = equation[0], equation[-1], equation[1:3]
            if operator == '==': 
                x, y = find(a), find(b)
                if x != y:
                    union[y] = x
                    
        # second pass, check validity
        for equation in equations:
            a, b, operator = equation[0], equation[-1], equation[1:3]
            if operator == '!=' and find(a) == find(b):
                return False
            
        return True