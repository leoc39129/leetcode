class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Base Case:
        if len(nums) == 1:
            return 1

        k = 0
        nums_dict = {}
        for idx in range(len(nums)):
            if nums[idx] not in nums_dict.keys():
                nums[k] = nums[idx]
                nums_dict[nums[idx]] = 1
                k += 1
        
        return k

'''
Got it quick! Modifying nums in place is the trick here, but we need some type
of way to check if a value is unique or not. That could be done by looking at
adjacent values because the array is sorted, but using more space is a simpler
more efficient solution. Let's check the discussion board for any creative solutions

This solution's interesting because instead of looking at i and i+1, it looks at
i and i-1 starting from i=1 due to the insight that nums[0] will always be in the
right place i.e., it's always unique. It's simply a two pointer approach -- which is
technically RT O(n), space O(1), while my current solution is O(n) in both 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
'''