from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class RecursiveSolution(object):
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


class BetterRecursiveSolution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
            


class IterativeSolution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                node.right, node.left = node.left, node.right
                q.append(node.right)
                q.append(node.left)

        return root


'''
RT: O(n)
Space: O(h) = O(n) for unbalanced trees

It's an easy problem for a reason! Got the better organized recursive and iterative solutions
in optimal time.
'''