# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        paths = []
        def path(node): 
            if not node.left and not node.right:
                return [[node.val]]
            res = []
            for child in node.left, node.right:
                if child:
                    for subpath in path(child):
                        res.append([node.val] + subpath)
            return res
        
        res = []
        for subpath in path(root):
            if sum(subpath) == targetSum:
                res.append(subpath)
        return res
            