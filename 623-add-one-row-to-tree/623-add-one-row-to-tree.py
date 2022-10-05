# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        nodes = [root]
        level = 2
        while level < depth:
            nodes = [child for node in nodes for child in (node.left, node.right) if child]
            level += 1
    
        for node in nodes:
            l, r = node.left, node.right
            node.left = TreeNode(val, l, None)
            node.right = TreeNode(val, None, r)
        
        return root