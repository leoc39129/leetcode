# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def __init__(self):
        self.cloned = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # Base Cases
        if not node:
            return None

        if node in self.cloned:
            return self.cloned[node]

        clone = Node(node.val)
        self.cloned[node] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))

        return clone

                
'''
RT: O(V+E)
Space: O(V)

This optimal solution uses a dictionary to track which nodes have been cloned already, and that
dictionary uses the original node as a key and the created node as a value. Here's an iterative solution,
which is better for large/very large graphs, as opposed to the recursive approach being more efficient
with smaller graphs


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        # A dictionary to store the mapping from original node to cloned node
        cloned = {}
        
        # Initialize the stack with the first node
        stack = [node]
        
        # Clone the first node and add it to the dictionary
        cloned[node] = Node(node.val)
        
        while stack:
            current = stack.pop()
            
            # Iterate through all neighbors of the current node
            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    # Clone the neighbor and add it to the dictionary
                    cloned[neighbor] = Node(neighbor.val)
                    # Add the neighbor to the stack for further processing
                    stack.append(neighbor)
                
                # Connect the current node's clone to the neighbor's clone
                cloned[current].neighbors.append(cloned[neighbor])
        
        return cloned[node]

'''