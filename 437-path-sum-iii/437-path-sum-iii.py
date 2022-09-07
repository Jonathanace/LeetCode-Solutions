# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.count = 0
        def check(node):
            if not node:
                return []
            l = check(node.left) + check(node.right)
            for i in l: 
                if i + node.val == targetSum:
                    self.count += 1
            if node.val == targetSum:
                self.count += 1
            l = [i + node.val for i in l]
            l.append(node.val)
            return l
    
        check(root)
        return self.count