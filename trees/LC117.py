"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        queue = deque([root])
        while queue:
            level = []  
            for _ in range(len(queue)): 
                node = queue.popleft()  
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            for idx in range(0, len(level)-1):
                level[idx].next = level[idx+1]

        return root

        
        
'''
RT: O(n)
Space: O(n)

There's a O(n) RT, O(1) Space algorithm below that essentially leverages the fact that you can
use the next pointers to traverse the level, rather than using a queue taking up space.


class Solution(object):
    def connect(self, root):
        if not root:
            return None

        # Initialize the start of the current level
        current = root

        while current:
            # Dummy node for the next level
            dummy = Node(0)
            tail = dummy  # Tail of the next level list
            
            # Traverse the current level
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                
                # Move to the next node in the current level
                current = current.next
            
            # Move to the next level
            current = dummy.next

        return root

'''