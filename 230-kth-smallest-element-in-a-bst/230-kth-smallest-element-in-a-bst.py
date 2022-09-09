# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        def check(node): 
            if node:
                l.append(node.val)
            if node.left:
                check(node.left)
            if node.right:
                check(node.right)
        check(root)
        return sorted(l)[k - 1]