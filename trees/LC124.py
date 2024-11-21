# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # def __init__(self):
    #     self.path_sum = 0

    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # The idea is to get the maximum path sum from the left,
        # then see if the root is positive (max path sum from the "root"),
        # then compare the left with the right
        if not root:
            return 0
    
        if not root.left and not root.right:
            return root.val

        left_no_root = self.recurse(root.left, float("-inf"))
        left_root = self.recurse(root.left, root.val)
        right_no_root = self.recurse(root.right, float("-inf"))
        right_root = self.recurse(root.right, root.val)

        return max(left_no_root, 
                    left_root,
                    left_root+right_root-root.val,
                    right_root,
                    right_no_root,
                    root.val)

    def recurse(self, node, path_sum):
        if not node:
            return path_sum

        if path_sum == float("-inf"):
            # This node can be the inflection point/"root" of the path
            return self.maxPathSum(node)
        else:
            # We already have an inflection point/"root"
            # see whether going left or right is more beneficial
            left = self.recurse(node.left, path_sum+node.val)
            right = self.recurse(node.right, path_sum+node.val)

            return max(left, right)


'''
So it ended up being that you can't pass the max_path down recursively, you have to hold it in 
a global var to keep track of it


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__ (self):
        self.max_path = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.dfs(root)
        return self.max_path
        
    def dfs(self, node):
        if not node:
            return 0
        
        # Recurse into left and right subtrees
        left_gain = max(self.dfs(node.left), 0)  # Ignore paths with negative sums
        right_gain = max(self.dfs(node.right), 0)
        
        # Calculate the maximum path sum passing through this node
        current_max = node.val + left_gain + right_gain
        
        # Update the global max_sum if the current path is the best
        self.max_path = max(self.max_path, current_max)
        
        # Return the maximum gain that can be extended to the parent
        return node.val + max(left_gain, right_gain)

'''