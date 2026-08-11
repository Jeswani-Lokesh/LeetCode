# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Two separate chains, each with its own dummy head
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less = less_dummy         # tail of the "< x" chain
        greater = greater_dummy   # tail of the ">= x" chain
        
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
        
        # Terminate the greater chain (avoid a cycle)
        greater.next = None
        # Stitch: end of less chain → start of greater chain
        less.next = greater_dummy.next
        
        return less_dummy.next
        