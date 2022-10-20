class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        IV = 4
        IX = 9
        
        XL = 40
        XC = 90
        
        CD = 400
        CM = 900
        '''
        res = []
        while num > 0:
            if num >= 1000:
                num -= 1000
                res.append('M')
            elif num >= 900:
                num -= 900
                res.append('CM')
            elif num >= 500:
                num -= 500
                res.append('D')
            elif num >= 400:
                num -= 400
                res.append('CD')
            elif num >= 100:
                num -= 100
                res.append('C')
            elif num >= 90:
                num -= 90
                res.append('XC')
            elif num >= 50: 
                num -= 50
                res.append('L')
            elif num >= 40:
                num -= 40
                res.append('XL')
            elif num >= 10:
                num -= 10
                res.append('X')
            elif num >= 9: 
                num -= 9
                res.append('IX')
            elif num >= 5:
                num -= 5
                res.append('V')
            elif num >= 4:
                num -= 4
                res.append('IV')
            else:
                num -= 1
                res.append('I')
        
        return ''.join(res)