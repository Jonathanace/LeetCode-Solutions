class Solution:
    def numsSameConsecDiff(self, length: int, difference: int) -> List[int]:
        
        res = set()
        for i in range(difference, 10):
            if i == 0:
                continue
            res.add(str(i))
            
        for i in range(1, 10-difference):
            res.add(str(i))
            
        res = list(res)
        difference = str(difference)
        count = 1
        while count < length:
            count += 1
            buff = []
            for i in res:
                # print(i)
                if int(i[-1]) + int(difference) < 10: 
                    buff.append(i + str(int(i[-1]) + int(difference)))
                if int(i[-1]) - int(difference) >= 0:
                    buff.append(i + str(int(i[-1]) - int(difference)))
            res = buff
            
        return sorted(list(set(res)))