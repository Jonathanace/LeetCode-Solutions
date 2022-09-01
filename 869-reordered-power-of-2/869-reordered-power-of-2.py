from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for i in [j for j in set([''.join(i) for i in permutations(str(n))]) if not j.startswith('0')]:
            binary = str(bin(int(i)))[2:]
            if binary.rstrip('0') == '1':
                return True
        return False