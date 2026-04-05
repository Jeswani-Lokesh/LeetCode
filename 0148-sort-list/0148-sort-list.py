# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If list is empty or has only one node, it's already sorted
        if not head or not head.next:
            return head

        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        prev = None

        # Move fast pointer twice as fast as slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Cut the list into two halves
        prev.next = None

        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)

        # Step 3: Merge the two sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        # Dummy node to simplify merging
        dummy = ListNode(0)
        tail = dummy

        # Merge two sorted lists
        while l1 and l2:
            # Pick the smaller value
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            # Move tail forward
            tail = tail.next

        # Attach remaining nodes
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        # Return merged list
        return dummy.next
        