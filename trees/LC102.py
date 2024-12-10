# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ret = []
        q = deque([root])

        while q:
            level_nodes = []
            while q:
                level_nodes.append(q.popleft())

            level_vals = []
            for node in level_nodes:
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level_vals.append(node.val)
            if len(level_vals) > 0:
                ret.append(level_vals)

        return ret
        