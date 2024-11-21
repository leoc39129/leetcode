# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return root

        root = self.recurse(root)

    def recurse(self, node):
        if not node.left and not node.right:
            return node

        ret = node
        
        temp = node.right
        if node.left:
            node.right = self.recurse(node.left)
            node.left = None
            while node.right:
                node = node.right

        if temp:
            node.right = self.recurse(temp)

        return ret


'''
RT: O(n)
Space: O(n) -- the recursive stack

Technically the iterative solution is the optimal one, as the problem asks for a
solution to "flatten the tree in place (with O(1) extra space)". So, here's a strange 
looking iterative solution:

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        current = root
        while current is not None:

            if current.left is not None:
                last = current.left
                while last.right is not None:
                    last = last.right

                last.right = current.right
                current.right = current.left
                current.left = None

            current = current.right
'''

                