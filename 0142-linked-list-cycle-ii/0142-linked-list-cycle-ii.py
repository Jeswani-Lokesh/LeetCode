# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        # Phase 1: detect whether a cycle exists
        while fast and fast.next:
            slow = slow.next          # 1 step
            fast = fast.next.next     # 2 steps
            if slow == fast:          # they met → cycle exists
                break
        else:
            # Loop ended without break → no cycle
            return None
        
        # Phase 2: find the entry node
        # Move one pointer back to head; advance both 1 step at a time.
        # They meet at the cycle's start.
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
        