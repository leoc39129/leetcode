# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        # Base Case
        if not root.left and not root.right:
            return [root.val]

        avgs = []
        q = deque([root])

        while q:
            level = []
            while q:
                level.append(q.popleft())
            
            nodes_sum = 0
            count = 0
            for node in level:
                if node:
                    nodes_sum += node.val
                    count += 1
                    q.append(node.left)
                    q.append(node.right)
            if count != 0:
                avgs.append(nodes_sum / count)

        return avgs
        
'''
RT: O(n)
Space: O(n)

Easy level order BFS traversal.
'''