class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.preorderSumNum(root, [])

    def preorderSumNum(self, node, digits):
        digits.append(node.val)

        if not node.left and not node.right:
            n = len(digits)-1
            exp = 1
            while n > 0:
                exp *= 10
                n -= 1
            dig_sum = 0

            for num in digits:
                dig_sum += exp*num
                exp /= 10
                
            return dig_sum
        
        left = 0
        right = 0
        if node.left:
            left = self.preorderSumNum(node.left, list(digits))

        if node.right:
            right = self.preorderSumNum(node.right, digits)

        # print(left)
        # print(right)

        return left + right
    
'''
RT: O(n)
Space: O(1)

Missed an insight, that you can just pass the value down, multiply it by ten and then
add the current node to preserve digit integrity. I love this discussion board solution.
When you need to keep track of a value (or anything really) while recursing, use an
__init__ fn to define it, and increment it with self.total += .. or self.arr.append(...)

class Solution(object):
    def __init__(self):
        self.total = 0
    
    def recurse(self, root, value):
        v = value * 10 + root.val
        if root.left is None and root.right is None:
            self.total += v
        if root.left:
            self.recurse(root.left, v)
        if root.right:
            self.recurse(root.right, v)
    
    def sumNumbers(self, root):
        if root is None:
            return 0
        self.recurse(root, 0)
        return self.total

    
Here's GPT's iterative DFS solution

class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        
        stack = [(root, 0)]  # (current node, current_sum)
        total_sum = 0
        
        while stack:
            node, current_sum = stack.pop()
            
            if node:
                current_sum = current_sum * 10 + node.val
                
                # If it's a leaf, add to total_sum
                if not node.left and not node.right:
                    total_sum += current_sum
                else:
                    # Push children to stack
                    if node.right:
                        stack.append((node.right, current_sum))
                    if node.left:
                        stack.append((node.left, current_sum))
        
        return total_sum

'''