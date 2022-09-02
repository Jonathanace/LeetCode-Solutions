# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nodes = [root]
        depth = [1]
        levels = defaultdict(list)
        
        for level, node in zip(depth, nodes): 
            levels[level].append(node.val)
            for child in node.left, node.right:
                if child:
                    nodes.append(child)
                    depth.append(level + 1)
                    
        res = []
        for key in levels.keys():
            res.append(sum(levels[key]) / len(levels[key]))
        return res