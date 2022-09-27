class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        last_fall = None
        last_fall_index = 0
        res = ['.'] * len(dominoes)
        for i in range(len(dominoes)):
            # print(dominoes[i])
            if dominoes[i] == 'L' and last_fall == 'R':
                num_between = i - last_fall_index - 1
                for j in range(last_fall_index+1, last_fall_index + num_between//2 + 1):
                    res[j] = 'R'
                for j in range(i-num_between//2, i):
                    res[j] = 'L'
                
                if num_between % 2 == 1:
                    res[last_fall_index + (num_between)//2 + 1] = '.'
            elif dominoes[i] == 'L':
                for j in range(last_fall_index, i):
                    res[j] = 'L'
            elif dominoes[i] == 'R' and last_fall == 'R':
                for j in range(last_fall_index, i):
                    res[j] = 'R'
            if dominoes[i] != '.':
                res[i] = dominoes[i]
                last_fall_index = i
                last_fall = dominoes[i]
                
            res[i] == dominoes[i]
        if last_fall == 'R':
            for i in range(last_fall_index, len(dominoes)): 
                res[i] = 'R'
        
                
        return ''.join(res)