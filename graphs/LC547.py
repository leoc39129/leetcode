class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        graph = {}
        visited = set()

        # populate our dictionary as the key being the node, and add all directly connected
        # nodes to its corresponding list
        n = len(isConnected)
        for i in range(n):
            graph[i] = []
            for j in range(n):
                if i == j:
                    pass
                elif isConnected[i][j] == 1:
                    graph[i].append(j)
    
        count = 0

        for key in graph:
            if key not in visited:
                # If you're here, you found a new province, so...
                # add one to count, add all nodes in that province to our set by calling dfs(key)
                # we add all nodes in the province to the set so we don't count the same province twice
                count += 1
                dfs(key)
            
        return count
            
                