# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Base Cases
        if not root:
            return None
        if root == p or root == q:
            return root

        l = self.traverse(root.left, p, q)
        if not l:
            return self.lowestCommonAncestor(root.right, p, q)

        r = self.traverse(root.right, p, q)
        if not r:
            return self.lowestCommonAncestor(root.left, p, q)

        if l and r:
            return root

            

    def traverse(self, root, p, q):
        if not root:
            return None

        if root == p or root == q:
            return root
        
        return self.traverse(root.left, p, q) or self.traverse(root.right, p, q)

            

'''
Just needed to realize that you don't need traverse. Here's the O(n) RT and space solution:

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Base case: if root is None or root is p or q
        if not root or root == p or root == q:
            return root

        # Recurse into the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, root is the LCA
        if left and right:
            return root

        # If one of them is non-null, return the non-null child
        return left if left else right

'''