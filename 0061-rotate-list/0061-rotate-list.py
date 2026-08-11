# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge cases: empty list or single node
        if not head or not head.next:
            return head
        
        # 1. Find length and the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # 2. Reduce k — rotating by length is a no-op
        k %= length
        if k == 0:
            return head
        
        # 3. Make it a circular list
        tail.next = head
        
        # 4. Find the new tail: (length - k - 1) steps from head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # 5. New head is right after new tail; break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head