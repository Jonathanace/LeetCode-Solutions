# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: # no node
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node if (node.left or node.right) or (node.val == 1) else None
        
        return dfs(root)