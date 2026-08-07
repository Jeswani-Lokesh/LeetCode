# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: no node or single node left
        if not head or not head.next:
            return head
        
        first = head
        second = head.next
        
        # Swap
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second