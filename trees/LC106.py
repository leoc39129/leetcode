class RecursiveSolution:
    def buildHelper(self, inorder, ins, inl, postorder, posts, postl, index):
        if posts > postl or ins > inl:
            return None
        
        # The last element of postorder is the root of the current subtree
        root = TreeNode(postorder[postl])

        # Find the index of the root in inorder traversal
        ind = index[root.val]
        
        # Number of nodes in the left subtree
        x = ind - ins

        # Recursively build the left and right subtrees
        root.left = self.buildHelper(inorder, ins, ind - 1, postorder, posts, posts + x - 1, index)
        root.right = self.buildHelper(inorder, ind + 1, inl, postorder, posts + x, postl - 1, index)

        return root

    def buildTree(self, inorder, postorder):
        # Map the values to their indices in inorder traversal
        index = {val: i for i, val in enumerate(inorder)}
        
        # Build the tree using the helper function
        return self.buildHelper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, index)


class IterativeSolution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None
        
        # Map value -> index in inorder for quick lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        root = TreeNode(postorder.pop())
        stack = [root]
        inorder_idx = len(inorder) - 1
        
        while postorder:
            node = stack[-1]
            if inorder_map[node.val] != inorder_idx:
                # Create the right child
                new_node = TreeNode(postorder.pop())
                node.right = new_node
                stack.append(new_node)
            else:
                # Pop nodes from the stack while they match the inorder traversal
                while stack and inorder_map[stack[-1].val] == inorder_idx:
                    node = stack.pop()
                    inorder_idx -= 1
                
                # Create the left child
                if postorder:
                    new_node = TreeNode(postorder.pop())
                    node.left = new_node
                    stack.append(new_node)
        
        return root


'''
Had the right ideas, but no idea how to build either iteratively or recursively (it can be done in both,
as seen above). Come back to this one!

On to the next.
'''