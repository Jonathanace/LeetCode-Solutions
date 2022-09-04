# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = [root]
        columns = [0]
        d = defaultdict(list)
        while root and level:
            buffer = []
            col_buff = []
            d_buff = defaultdict(list)
            # print([node.val for node in level], columns)
            for node, column in zip(level, columns):
                d_buff[column].append(node.val)
                if node.left:
                    buffer.append(node.left)
                    col_buff.append(column - 1)
                if node.right:
                    buffer.append(node.right)
                    col_buff.append(column + 1)
            level = buffer
            columns = col_buff
            for key in d_buff.keys():
                d[key].extend(sorted(d_buff[key]))

        return [d[key] for key in sorted(d.keys())]
        
        