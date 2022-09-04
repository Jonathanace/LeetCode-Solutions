# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # 345 ms, faster than 96.39% 
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return empty if linked list doesn't exist
        if not head:
            return None
        
        # convert linked list to python list
        l = []
        while head: # O(n)
            l.append(head)
            head = head.next
        
        # sort python list by node values
        l.sort(key = lambda x: x.val) # O(nlogn)
        
        # re-link nodes by order in value-sorted python list
        for i in range(0, len(l) - 1): # O(n)
            l[i].next = l[i + 1]
        
        l[-1].next = None # set last node to point to none
        return l[0] # return head of newly linked list