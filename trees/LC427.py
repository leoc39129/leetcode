
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        root = None
        n = len(grid)
        #print(grid)
        if n == 1:
            if grid[0][0] == 0:
                temp = False
            else:
                temp = True
            node = Node(val=temp, isLeaf=True)
            return node
        else:
            # for num in range(0, n, n/2):
            #     self.construct(grid[num:num+n/2][num:num+n/2])
            condition = True
            val = grid[0][0]
            for row in range(n):
                for col in range(n):
                    if grid[row][col] != val:
                        condition = False
                        break
            if not condition:
                tLeft = [row[:n/2] for row in grid[:n/2]]
                tRight = [row[n/2:n] for row in grid[:n/2]]
                bLeft = [row[:n/2] for row in grid[n/2:n]]
                bRight = [row[n/2:n] for row in grid[n/2:n]]
                return Node(val=False, isLeaf=False,
                            topLeft=self.construct(tLeft), 
                            topRight=self.construct(tRight),
                            bottomLeft=self.construct(bLeft), 
                            bottomRight=self.construct(bRight))
            else:
                return Node(val=val, isLeaf=True)

        return None
            
        