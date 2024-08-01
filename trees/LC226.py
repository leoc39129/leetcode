# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inv_recurse(start):
            if start == None or (start.left == None and start.right == None):
                return start
            temp = start.right
            start.right = inv_recurse(start.left)
            start.left = inv_recurse(temp)
            return start
    
        return inv_recurse(root)
            