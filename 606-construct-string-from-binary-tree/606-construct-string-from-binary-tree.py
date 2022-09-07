# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            if node.left and node.right:
                return f'{node.val}({preorder(node.left)})({preorder(node.right)})'
            elif node.left: # only left
                return f'{node.val}({preorder(node.left)})'
            elif node.right: # only right
                return f'{node.val}()({preorder(node.right)})'
            else: # no nodes
                return f'{node.val}'
        
        return preorder(root)