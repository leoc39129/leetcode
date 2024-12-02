# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.root = root
        
        self.half = deque([])
        self.buildHalf(root.left)
        self.half.append(root.val)

    def buildHalf(self, node):
        if not node:
            return
        self.buildHalf(node.left)
        self.half.append(node.val)
        self.buildHalf(node.right)
    
    def next(self):
        """
        :rtype: int
        """
        if len(self.half) > 0:
            ret = self.half.popleft()
        if ret == self.root.val:
            # self.half = deque([])
            self.buildHalf(self.root.right)
        return ret
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.half) > 0:
            return True
        return False 
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

'''
Got a correct solution with O(1) next and hasNext, but using O(n/2)=O(n) memory. The optimal
approach, using only O(h) storage, involves only storing the current root to leaf path
using a stack. See below:

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._leftmost_inorder(root)
    
    def _leftmost_inorder(self, node):
        """
        Push all the left nodes of the current subtree onto the stack.
        """
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self):
        """
        :rtype: int
        """
        # Pop the top node
        topmost_node = self.stack.pop()
        
        # If the node has a right child, process its left subtree
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        
        return topmost_node.val
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
'''