class Solution: # solution from https://leetcode.com/problems/gas-station/discuss/1705893/Python3-DEBIT-AND-CREDIT-O(1)-SPACE-(-)-Explained
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        candidate = None
        credit = 0
        debit = 0
        for i in range(len(gas)):
            credit += gas[i] - cost[i]
            if credit < 0:
                candidate = None
                debit = debit - credit
                credit = 0
            elif candidate is None:
                candidate = i
                
        if credit >= debit:
            return candidate
        else:
            return -1