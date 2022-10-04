# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recur(node, prev_sum):
            # no node
            if not node:
                return
            
            # leaf node
            if not node.left and not node.right:
                if node.val + prev_sum == targetSum:
                    return True
                
            # internal node
            return True if recur(node.left, prev_sum + node.val) or recur(node.right, prev_sum + node.val) else False
        
        return recur(root, 0)