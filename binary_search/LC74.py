class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)         # rows
        if m == 0:
            return False
        
        n = len(matrix[0])      # cols
        if n == 0:
            return False

        # Base Case:
        if m == 1 and n == 1:
            return target == matrix[0][0]

        # Binary search!
        cur = matrix[m // 2]
        low = cur[0]
        high = cur[-1]
        if target < low:
            return self.searchMatrix(matrix[0:m//2], target)
        elif target > high:
            return self.searchMatrix(matrix[(m//2)+1:], target)
        else:
            # Target must be in this row
            return self.binSearchList(matrix[m//2], target)

        return False

    def binSearchList(self, lst, target):
        n = len(lst)
        if n == 0:
            return False
        if n == 1:
            return lst[0] == target
        
        pivot = lst[n // 2]
        if target < pivot:
            return self.binSearchList(lst[:n//2], target)
        elif target > pivot:
            return self.binSearchList(lst[(n//2)+1:], target)
        else:
            # pivot == target
            return True

'''
RT: O(log(n) + log(m)) == O(log(mn))
Space: O(1)

Good job adjusting on the fly, understanding the problem, and getting it done

Discussion board solutions are the same
'''