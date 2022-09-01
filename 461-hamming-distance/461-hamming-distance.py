class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        str_x = str(bin(x))[2:]
        str_y = str(bin(y))[2:]
        # print(str_x)
        # print(str_y)
        
        if len(str_x) > len(str_y):
            str_y = '0' * abs(len(str_x) - len(str_y)) + str_y
            
        elif len(str_y) > len(str_x): 
            str_x = '0' * abs(len(str_y) - len(str_x)) + str_x
            
        else:
            # they're the same length
            pass
        
        
        # print(str_x, str_y)
        res = 0
        for i in range(len(str_x)): 
            if str_x[i] != str_y[i]:
                res += 1
                
        return res