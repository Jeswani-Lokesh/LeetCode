# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head       # Moves 1 step
        fast = head       # Moves 2 steps

        # Traverse the list while fast pointer can move
        while fast and fast.next:
            slow = slow.next          # Move slow by 1
            fast = fast.next.next     # Move fast by 2

            if slow == fast:
                return True  # Pointers met → cycle detected

        # If fast reached end → no cycle
        return False
        