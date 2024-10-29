# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Base Case:
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])

        idx = 0
        left_stack = []
        while inorder[idx] != preorder[0]:
            # Build left subtree
            left_stack.append(inorder[idx])
        while len(left_stack) > 2:
            left = TreeNode(left_stack.pop())
            center_val = left_stack.pop()
            right = TreeNode(left_stack.pop())
            center = TreeNode(center_val, left, right)
        root.left = center
        return root


'''
Short on time here, got the initial concept but couldn't execute. See db soln

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
        mapping = {}

        for i in range(len(inorder)):
            mapping[inorder[i]] = i
        
        preorder = collections.deque(preorder)

        def build(start, end):
            if start > end: return None

            root = TreeNode(preorder.popleft())
            mid = mapping[root.val]

            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)

            return root

        return build(0, len(preorder) - 1)
'''   
