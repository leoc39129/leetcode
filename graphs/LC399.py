from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Make a dictionary of dictionaries to represent a directed graph
        graph = defaultdict(dict)
        for idx in range(len(equations)):
            num = equations[idx][0]
            denom = equations[idx][1]
            graph[num][denom] = values[idx]
            graph[denom][num] = 1 / values[idx] 
        
        def dfs(num, denom, visited, current_product):
            # If the numerator and denominator are the same, return the current product
            if num == denom:
                return current_product
            
            visited.add(num)
            
            # Explore neighbors
            for neighbor, value in graph[num].items():
                if neighbor not in visited:
                    result = dfs(neighbor, denom, visited, current_product * value)
                    if result != -1.0:  # Found a valid path to the denominator
                        return result
            
            return -1.0  # No valid path found

        res = []
        for idx in range(len(queries)):
            num = queries[idx][0]
            denom = queries[idx][1]

            if num not in graph or denom not in graph:
                res.append(-1.0)
            elif num == denom:
                res.append(1.0)
            else:
                res.append(dfs(num, denom, set(), 1.0))

        return res


'''
Good intro to graphs. Almost got it fully, minus writing the actual DFS function,
which I guess is the actual tough part. Study this one before moving onto the next
graph problem.
'''