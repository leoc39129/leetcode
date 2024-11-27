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
Revisited this problem with a similar result, but at least I understand the discussion board solution now

RT: O(log(n)*log(n))
Space: O(log(n)) -- this tree is not always perfectly balanced, but it will never be unbalanced
    space is then O(tree height) = O(h) = O(log(n))

Even for some smaller cases, not all nodes are "visited" in the recursive stack. In Example 1 that the problem
gives, nodes 4 and 5 will not be "visited" with their own recursive call. Instead, the recursive call where root=2
will find a perfect subtree of 3 nodes. All of the other nodes in that example will be visited, but you can see the
runtime benefits if you had a tree like ...

          1
       /     \
      2        3
     / \      / \
    4   5    6   7
   / \ / \  / \ / \
  8  910 11


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
'''
            

        