# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def inorder(node, prev_val):
            # check to see if we're at a null node
            if node == None:
                return True
            # check left node
            print(node.val)
            print(prev_val)
            if inorder(node.left, prev_val) == False:
                return False
            print(node.val)
            print(prev_val)
            # check to see if current node (left value) is less than prev_val, or the root
            if node.val <= prev_val[0]:
                return False
            # if we get to here, now we just need to validate right part of the tree
            prev_val[0] = node.val
            return inorder(node.right, prev_val)

        prev_val = [float('-inf')]
        return inorder(root, prev_val)
    
        