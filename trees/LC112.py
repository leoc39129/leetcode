# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

'''
RT: O(n)
Space: O(H), where H is the height of the tree

This is an optimal solution!

Here's GTP's iterative solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        # Stack stores pairs of (node, remaining sum)
        stack = deque([(root, targetSum)])

        while stack:
            node, current_sum = stack.pop()

            # Check if it's a leaf node with the required sum
            if not node.left and not node.right:
                if current_sum == node.val:
                    return True

            # Push left and right children with updated sums onto the stack
            if node.right:
                stack.append((node.right, current_sum - node.val))
            if node.left:
                stack.append((node.left, current_sum - node.val))

        return False

'''
        