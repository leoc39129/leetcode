# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class IterativeSolution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        q = deque([root])
        depth = 0
        while q:
            level = []
            while q:
                level.append(q.popleft())

            if len(level) != 0:
                depth += 1

            for node in level:
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

        return depth


class RecursiveSolution(object):
    def maxDepth(self, root, level=0):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return level
        
        return max(self.maxDepth(root.left, level+1), self.maxDepth(root.right, level+1))


class MoreComplicatedRecursiveSolution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        return self.recurse(root, 0)

    def recurse(self, root, depth):
        if not root:
            return depth

        l = root
        lDepth = 1
        while l.left:
            l = l.left
            lDepth += 1

        r = root
        rDepth = 1
        while r.right:
            r = r.right
            rDepth += 1

        return max(self.recurse(root.left, depth+1), self.recurse(root.right, depth+1))


class WayTooComplicatedRecursiveSolution(object):
    def __init__(self):
        self.curMaxDepth = 0

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.recurse(root, 0)
        return self.curMaxDepth

    def recurse(self, root, depth):
        if not root:
            return

        l = root
        lDepth = 1
        while l.left:
            l = l.left
            lDepth += 1

        r = root
        rDepth = 1
        while r.right:
            r = r.right
            rDepth += 1

        self.curMaxDepth = max(self.curMaxDepth, rDepth+depth, lDepth+depth)
        self.recurse(root.left, depth+1)
        self.recurse(root.right, depth+1)


'''
RT: O(n)
Space: O(h) -- worst case O(n)

Easy problem, tried to duplicate a solution from finding the depth of a complete tree (which is
O(logn*logn) runtime), but I forgot that being an unbalanced tree, that algorithm runs in worst
case O(n).
'''
            
        

        
        
            
        

        
        
        
        