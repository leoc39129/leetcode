class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        k = 2
        for idx in range(2, len(nums)):
            if nums[idx] != nums[k-2]:
                nums[k] = nums[idx]
                k += 1

        return k
            
'''
Had some decent insights, but no cohesive solution. Missed a critical insight, that the 
first two elements in the array don't matter, so just start looking at idx=2 to see if
you need to start replacing, and go from there. Actually, that insight wasn't missed,
it was simply overlooked after the base case was written -- leverage your base case
in your code!

We'll get em next time
'''