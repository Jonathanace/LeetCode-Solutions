# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node: 
                return 0
            else:
                l = check(node.left)
                r = check(node.right)
                if l - r < -1 or l - r > 1:
                    return float('inf')
                else: 
                    return max(l, r) + 1
            
        return False if check(root) == float('inf') else True