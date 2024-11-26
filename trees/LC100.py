# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # Base Case:
        if not p:
            return not q
        if not q:
            return not p

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False

'''
RT: O(n)
Space: O(n) (worst case, O(h)==O(logn) in most cases where the tree is balanced)

Nice and easy, recursive preorder traversal of the tree to validate that the both of them are the same.
This can also be done iteratively, but it will also have the same runtime and space complexities
'''
        