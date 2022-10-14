# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        
        while head:
            l.append(head)
            head = head.next
        
        if len(l) == 1:
            return None
        
        mid = (len(l))//2
        l.pop(mid)
        
        if mid == len(l):
            l[mid-1].next = None
        else:
            l[mid-1].next = l[mid]
        
        return l[0]