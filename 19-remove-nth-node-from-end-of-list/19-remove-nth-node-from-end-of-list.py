# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # 34 ms, faster than 93.53%
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = []
        i = head
        while i:
            l.append(i)
            i = i.next
        if len(l) - n == 0: # removing head
            return head.next
        elif len(l) == n: # removing tail
            l[-2].next = None 
        else: # removing internal node
            l[len(l)-n-1].next = l[len(l)-n].next
        return head