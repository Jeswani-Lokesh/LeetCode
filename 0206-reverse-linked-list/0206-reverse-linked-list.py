# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None         # Initially, previous node is None (end of reversed list)
        curr = head         # Start with the head of the list

        while curr:
            next_node = curr.next  # Temporarily store the next node
            curr.next = prev       # Reverse the pointer
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward

        return prev  # New head of the reversed list
        