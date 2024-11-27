from collections import defaultdict

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        # Base Case
        if len(bank) == 0:
            return -1

        # Assuming that endGene is in bank, because all valid gene mutations are in
        # bank, and it's not a given that endGene is a valid mutation
        if endGene not in bank:
            return -1 

        if self.strDiff(startGene, endGene) == 1:
            return 1

        graph = defaultdict(list)
        graph[startGene] = []

        for gene in bank:
            graph[gene] = []
            if self.strDiff(startGene, gene) == 1:
                graph[startGene].append(gene)

        for i in range(len(bank)):
            for j in range(len(bank)):
                if i == j:
                    continue
                elif self.strDiff(bank[i], bank[j]) == 1:# and bank[i] not in graph[bank[j]]:
                    graph[bank[i]].append(bank[j])

        # print(graph)
        # Graph has been built, now we need to find the shortest path between 
        # startGene and endGene -- BFS w/ cycles in the graph
        diff = 0
        neighbors = graph[startGene]
        visited = set()
        while True:
            if endGene in neighbors:
                return diff+1
            elif len(neighbors) == 0:
                return -1
            temp = []
            for neighbor in neighbors:
                if neighbor in visited:
                    return -1
                visited.add(neighbor)
                lst = graph[neighbor]
                for node in lst:
                    temp.append(node)
            diff += 1
            neighbors = temp

        return diff


    def strDiff(self, str1, str2):
        diff = 0
        for i in range(8):
            if str1[i] != str2[i]:
                diff += 1

        return diff


'''
Damn close. I was on the right track, but a while loop is not the way to go for the BFS,
it's a queue. See GPT solution below

from collections import defaultdict, deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        # Base Case
        if endGene not in bank:
            return -1 

        # Build the graph
        graph = defaultdict(list)
        bank = set(bank)  # For O(1) lookups

        for gene in bank:
            if self.strDiff(startGene, gene) == 1:
                graph[startGene].append(gene)
            for other_gene in bank:
                if self.strDiff(gene, other_gene) == 1:
                    graph[gene].append(other_gene)

        # BFS to find the shortest path
        queue = deque([(startGene, 0)])  # (current gene, mutation count)
        visited = set()

        while queue:
            current_gene, mutations = queue.popleft()

            # If we reach the end gene, return the mutation count
            if current_gene == endGene:
                return mutations

            # Mark the current gene as visited
            visited.add(current_gene)

            # Traverse neighbors
            for neighbor in graph[current_gene]:
                if neighbor not in visited:
                    queue.append((neighbor, mutations + 1))

        # If we exhaust the BFS queue, there's no valid path
        return -1

    def strDiff(self, str1, str2):
        return sum(1 for a, b in zip(str1, str2) if a != b)

'''

        
        
        


        