"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def recurz(start, order):
            if(start == None):
                return None
            order.append(start.val)
            for x in range(0, len(start.children)):
                recurz(start.children[x], order)
            return order
        
        return recurz(root, [])