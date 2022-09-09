# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.l = [-float('inf')]
        stack = []
        node = root
        while node or stack: 
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                self.l.append(node)
                node = node.right
        # print(self.l)
        self.i = 0
    def next(self) -> int:
        self.i += 1
        return self.l[self.i].val

    def hasNext(self) -> bool:
        return True if self.i != len(self.l) - 1 else False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()