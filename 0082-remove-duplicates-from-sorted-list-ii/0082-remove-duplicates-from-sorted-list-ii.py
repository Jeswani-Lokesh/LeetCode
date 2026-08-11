# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy          # last node known to be unique
        curr = head
        
        while curr:
            # If curr is the start of a run of duplicates
            if curr.next and curr.val == curr.next.val:
                # Skip the entire run
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # prev links past the whole run
                prev.next = curr.next
            else:
                # curr is unique, advance prev
                prev = prev.next
            
            curr = curr.next
        
        return dummy.next
        