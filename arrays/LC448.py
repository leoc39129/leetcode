class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numset = set(nums)
        rangeset = set(range(1, len(nums)+1))
        res = list(rangeset.difference(numset))
        return res
                
            
        