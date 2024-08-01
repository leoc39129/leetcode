# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = [root]
        result = []
        direction = 1

        while q:
            temp = q
            q = []
            lvl = []
            for node in temp:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                lvl.append(node.val)

            direction *= -1
            if(direction > 0):
                lvl = lvl[::-1]
            result.append(lvl)
        return result
        
