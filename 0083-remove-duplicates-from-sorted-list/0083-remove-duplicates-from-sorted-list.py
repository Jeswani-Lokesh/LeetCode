# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
                # Pointer to traverse the list
        current = head

        # Traverse while next node exists
        while current and current.next:
            if current.val == current.next.val:
                # Duplicate found → skip next node
                current.next = current.next.next
            else:
                # Move to next unique node
                current = current.next

        return head
        
