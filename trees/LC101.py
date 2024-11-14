# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class IterativeSolution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Level order traversal
        q = deque([root])
        while q:
            level = []
            while q:
                level.append(q.popleft())
            # Check level symmetry
            if not self.checkSymmetry(level):
                return False
            
            for node in level:
                if node:    
                    q.append(node.left)
                    q.append(node.right)

        return True

    def checkSymmetry(self, level):
        if len(level) == 1:
            return True
        
        l = 0
        r = len(level)-1
        while l < r:
            if level[l] and level[r]:
                if level[l].val != level[r].val:
                    return False
            else:
                # We have one null node
                if level[l] or level[r]:
                    return False
            r -= 1
            l += 1

        return True


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class RecursiveSolution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.recursiveSymTree([root.left, root.right])

    def recursiveSymTree(self, level):
        if len(level) == 0:
            return True

        l = 0
        r = len(level)-1
        while l < r:
            if level[l] and level[r]:
                if level[l].val != level[r].val:
                    return False

            else:
                # one null node
                if level[l] or level[r]:
                    return False

            l += 1
            r -= 1

        new_level = []
        for node in level:
            if node:
                new_level.append(node.left)
                new_level.append(node.right)

        return self.recursiveSymTree(new_level)
        
'''
RT: O(n)
Space: O(n)
(for both)

Silly mistakes! If you hit a bug, it's there. TLE means something IS wrong. Follow the program,
you'll find the error. Besides that slight hitch, good job figuring out level order traversal both
recursively and iteratively.

Here's a good discussion board soln

class Solution(object):
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)
'''


        

        
        

        