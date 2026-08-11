# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node just before position `left`
        for _ in range(left - 1):
            prev = prev.next
        
        # `curr` is the first node of the sublist to reverse
        curr = prev.next
        
        # Reverse by repeatedly moving the node after curr
        # to the front of the sublist (head-insertion)
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummy.next
        