# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Return the rightmost node on each level in increasing level order
        # Base Case:
        if not root:
            return []

        queue = deque([root])
        ret = []

        while queue:
            ret.append(queue[0].val)

            level = []
            while queue:
                cur = queue.popleft()
                if cur.right:
                    level.append(cur.right)
                if cur.left:
                    level.append(cur.left)

            for node in level:
                queue.append(node)
                
        return ret

        
'''
RT: O(n)
Space: O(h) -- worst case O(n)

You can also do this recursively, I find level order to be more straightforward 
when it's done iteratively. Here's a recursive GPT solution:


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []  # This will hold the rightmost nodes at each level
        self.dfs(root, 0)  # Start DFS from the root at level 0
        return self.result

    def dfs(self, node, level):
        """
        Helper function to perform DFS and track rightmost nodes.
        :type node: TreeNode
        :type level: int
        """
        if not node:
            return
        
        # If we're visiting a new level for the first time, add the node
        if level == len(self.result):
            self.result.append(node.val)
        
        # Recurse into the right subtree first, then the left subtree
        self.dfs(node.right, level + 1)
        self.dfs(node.left, level + 1)

'''