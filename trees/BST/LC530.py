# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def recurse(node, prev):
            if not node:
                return 1000000 
            elif node.val > prev:
                # We went down to the right, check the left with prev
                if not node.left and not node.right:
                    # There's no child nodes
                    return node.val - prev
                elif node.left and not node.right:
                    # There's a left child, no right child
                    return min(recurse(node.left, prev), node.left.val - prev)
                elif not node.left and node.right:
                    # There's a right child, no left child
                    return min(recurse(node.right, node.val), node.right.val - node.val)
                else:
                    # There are two children
                    return min(recurse(node.right, node.val), recurse(node.left, node.val), )

            else:
                # node.val < prev
                # We went down to the left, check the right with prev
                if not node.left and not node.right:
                    # There's no child nodes
                    pass
                elif node.left and not node.right:
                    # There's a left child, no right child
                    pass
                elif not node.left and node.right:
                    # There's a right child, no left child
                    pass
                else:
                    # There are two children
                    pass
    
        return recurse(root, 1000000)
    

'''
WOW that is an ugly piece of code. The key to this is to do an in order traversal of the BST
AKA if a node has two children, visit left, the node, then right. It works!

    4
   / \
  2   6
 / \
1   3

Visualize it with this example:

The in-order traversal visits the nodes in the order: 1 → 2 → 3 → 4 → 6.

At each step, the difference between the current node and the previous node is calculated:

2-1=1, 3-2=1, 4-3=1, 6-4=2
min = 1

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Initialize previous node and minimum difference
        self.prev = None
        self.min_diff = float('inf')
        
        # Helper function to perform in-order traversal
        def inorder(node):
            if not node:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Process the current node
            if self.prev is not None:
                # Calculate the difference with the previous node
                self.min_diff = min(self.min_diff, node.val - self.prev.val)
            
            # Update the previous node to the current node
            self.prev = node
            
            # Traverse the right subtree
            inorder(node.right)
        
        # Start the in-order traversal
        inorder(root)
        
        return self.min_diff

'''