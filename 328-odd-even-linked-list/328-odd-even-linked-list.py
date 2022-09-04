# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = []
        evens = []
        c = 1
        
        # first pass
        while head:
            if c&1: # if c is odd
                odds.append(head)
            else: # if c is even
                evens.append(head)
            head = head.next
            c += 1
        
        # link odds and evens
        for i in range(0, len(odds) - 1): 
            odds[i].next = odds[i + 1]
        for i in range(0, len(evens) - 1): 
            evens[i].next = evens[i + 1]
        
        # connect odds and evens
        try:
            odds[-1].next = evens[0]
        except:
            pass
        
        # set end of evens
        try:
            evens[-1].next = None
        except:
            pass
        
        # return
        if odds:
            return odds[0]
        if evens:
            return evens[0]
        return None
            