# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0

        count = 1
        node = root
        level_num = 1
        level = 0

        def recursiveCompleteTree(node, level):
            if node.right:
                # If there's a rightmost node, it means the level is complete
                count = count + 2*level_num
                level_num = level_num*2
                recursiveCompleteTree(node.right)
                recursiveCompleteTree(node.left)

                # If there isn't a rightmost node, the level is incomplete
                # But how incomplete?

            elif node.left:
                count = count + 1

            else:
                pass

        recursiveCompleteTree(node, level)

        # Switch up the approach: We know the left side of the tree will be full,
        # so we just need to know when is the first occurence of a right node missing
        # from either the left or right side

        # Once we know that, we'll know exactly how many nodes are in the tree

        # This should probably be done recursively?

        
        return count
    

'''
Discussion board solution:

class Solution(object):
    def countNodes(self, root, l=1, r=1):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: 
            return 0
        
        left = right = root    

        while left.left is not None:
            left = left.left
            l += 1  

        while right.right is not None:
            right = right.right
            r += 1           

        if l == r : return 2**l - 1                   
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

What I don't get about this is we end up looking at all N nodes anyway for the first example on LC -- I guess O(N) = O(( log(N) )^2)
only in that case? Look at it for larger cases, understand the methods for it, redo in your own work later
'''
            

        