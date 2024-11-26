from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Base Case:
        if len(prerequisites) == 0:
            return True

        graph = defaultdict(dict)

        for idx in range(len(prerequisites)):    
            graph[prerequisites[idx][1]][prerequisites[idx][0]] = 1

        # The graph has been created, now we have to see if there are any cycles
        def dfs(num, path, visited):
            for neighbor, num in graph[num].items():
                if path > numCourses:
                    return False
                if neighbor in visited:
                    return True
                if not dfs(neighbor, path+1, visited):
                    return False
            return True

        visited = set()
        for num in range(numCourses):
            if not dfs(num, 1, visited):
                return False
            visited.add(num)

        return True
        

'''
Very close to a full solution, but not quite. Had all the right ideas, just couldn't implement
detection of a cycle in a directed, unconnected graph. Here's the O(V+E) RT, O(V) space solution


from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Build the graph
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # Sets to track visited nodes
        visited = set()  # Fully processed nodes
        recStack = set()  # Nodes in the current recursion stack

        def dfs(node):
            # If the node is in the current stack, a cycle is detected
            if node in recStack:
                return False
            # If the node is already fully processed, no cycle
            if node in visited:
                return True

            # Add the node to the recursion stack
            recStack.add(node)

            # Recur for all neighbors
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            # Remove the node from the recursion stack and mark as visited
            recStack.remove(node)
            visited.add(node)

            return True

        # Check for cycles in each component
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False

        return True


Using Kahn's Algorithm...

from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Step 1: Build the graph and compute indegrees
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Step 2: Collect nodes with indegree 0
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        # Step 3: Process nodes in the queue
        processed = 0  # Count of processed nodes
        
        while queue:
            node = queue.popleft()
            processed += 1
            
            # Reduce indegree of neighbors and add them if their indegree becomes 0
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all nodes were processed
        return processed == numCourses


and here's a slightly more optimized discussion board solution

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre = defaultdict(list)

        for course, p in prerequisites:
            pre[course].append(p)
        
        taken = set()

        def dfs(course):
            if not pre[course]:
                return True
            
            if course in taken:
                return False
            
            taken.add(course)

            for p in pre[course]:
                if not dfs(p): return False
            
            pre[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
'''