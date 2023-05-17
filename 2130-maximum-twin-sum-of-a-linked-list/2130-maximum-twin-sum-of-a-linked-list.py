# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = []
        while head:
            l.append(head.val)
            head = head.next
            
        n = len(l)
        res = 0
        for i in range(0, n // 2):
            res = max(res, l[i] + l[-i - 1])
            
        return res