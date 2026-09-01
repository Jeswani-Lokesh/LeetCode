"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # `leftmost` is the first node of the current level we're processing
        leftmost = root
        
        while leftmost:
            # Dummy node: its .next will point to the first node of the NEXT level.
            # `tail` walks along, appending children as we find them.
            dummy = Node(0)
            tail = dummy
            
            # Traverse the current level via already-built next pointers
            curr = leftmost
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next        # move right along current level
            
            # dummy.next is the leftmost node of the next level
            leftmost = dummy.next
        
        return root
        