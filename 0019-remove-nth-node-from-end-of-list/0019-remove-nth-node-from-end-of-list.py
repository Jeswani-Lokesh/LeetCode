# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the length of the linked list
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        # If removing the head node
        if length == n:
            return head.next

        # Move to the node before the one to delete
        current = head

        for _ in range(length - n - 1):
            current = current.next

        # Remove the target node
        current.next = current.next.next

        return head