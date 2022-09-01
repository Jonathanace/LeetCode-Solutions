# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def traverse(node, prev_max):
            if not node:
                return
            if node.val >= prev_max:
                self.res += 1
            prev_max = max(prev_max, node.val)
            traverse(node.left, prev_max)
            traverse(node.right, prev_max)
            
        traverse(root, root.val)
        return self.res