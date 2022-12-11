# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        full_paths = set()
        def traverse(node):
            if not node:
                return 0
            
            l_path = traverse(node.left)
            r_path = traverse(node.right)  

            combined_path = l_path + r_path + node.val
            
            
            half_path = max([node.val, node.val+l_path, node.val+r_path])
            full_paths.add(combined_path)
            full_paths.add(node.val)
            full_paths.add(half_path)
            
            return half_path
                    
        return max(traverse(root), max(full_paths))