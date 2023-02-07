# solution via https://leetcode.com/problems/fruit-into-baskets/discuss/170740/JavaC%2B%2BPython-Sliding-Window-for-K-Elements
class Solution:
    def totalFruit(self, tree):
        count = {}
        i = 0
        for index, fruit in enumerate(tree):
            count[fruit] = count.get(fruit, 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
        return index - i + 1