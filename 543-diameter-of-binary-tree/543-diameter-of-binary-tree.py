# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        def check(node):
            if not node:
                return 0
            else:
                l = check(node.left)
                r = check(node.right)
                self.max = max(self.max, l + r)
                return max(l, r) + 1
            
        check(root)
        return self.max