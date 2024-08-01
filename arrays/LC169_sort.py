class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums) / 2
        nums.sort()
        cur = 1
        
        for x in range(0, len(nums)-1):
            if nums[x] == nums[x+1]:
                cur += 1
            else:
                cur = 1
            if cur > count:
                return nums[x]
        return nums[0]
        