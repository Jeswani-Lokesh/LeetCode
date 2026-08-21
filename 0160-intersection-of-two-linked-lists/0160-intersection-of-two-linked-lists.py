# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        a, b = headA, headB
        
        # When a pointer hits the end, redirect it to the OTHER list's head.
        # Both pointers travel lenA + lenB total, so they align.
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        
        # Either the intersection node, or None (both hit end together)
        return a
        