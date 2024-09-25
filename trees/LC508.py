# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # So I'm thinking collect all the possible sums in a dictionary
        # then find the most frequent from that dictionary

        # This can definitely be highly recursive

        # Base Case: We will have at least one node as the root of the tree
        sums = {}

        def sumNodes(node):
            # Given a TreeNode object node, return the subtree sum (int)
            cur_sum = node.val
            if node.left:
                cur_sum += sumNodes(node.left)
            if node.right:
                cur_sum += sumNodes(node.right)
            
            if cur_sum not in sums.keys():
                sums[cur_sum] = 1
            else:
                sums[cur_sum] += 1
                
            return cur_sum

        sumNodes(root)

        temp_max = -1
        ret = []

        # After calling the recursive function, sift through the dictionary
        # to find the most frequent subtree sum(s)

        for val in sums.keys():
            # print(val)
            # print(sums[val])
            if sums[val] > temp_max:
                ret = [val]
                temp_max = sums[val]
            elif sums[val] == temp_max:
                ret.append(val)

        return ret
        
        