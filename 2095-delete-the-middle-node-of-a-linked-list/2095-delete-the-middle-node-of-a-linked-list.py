# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # If only one node exists
        # deleting middle means empty list
        if not head.next:
            return None

        # Slow pointer
        slow = head

        # Fast pointer
        fast = head

        # Previous node before slow
        prev = None

        # Move pointers
        while fast and fast.next:

            # Store previous node
            prev = slow

            # Slow moves 1 step
            slow = slow.next

            # Fast moves 2 steps
            fast = fast.next.next

        # Delete middle node
        prev.next = slow.next

        # Return head
        return head        
        