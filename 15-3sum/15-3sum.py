class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        pos, zero, neg = [], [], []
        for num in nums: 
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
            else:
                zero.append(num)
                
        pos_set, neg_set = set(pos), set(neg)
        
        if zero:
            for num in pos:
                if -1 * num in neg_set:
                    res.add((0, -1 * num, num))
                
        if len(zero) >= 3:
            res.add((0, 0, 0))
            
        # negative pairs
        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                target = -1 * (neg[i] + neg[j])
                if target in pos_set:
                    res.add(tuple(sorted([target, neg[i], neg[j]])))
        
        # positive pairs
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                target = -1 * (pos[i] + pos[j])
                if target in neg_set:
                    res.add(tuple(sorted([target, pos[i], pos[j]])))
        
        return res