class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runsum = 0
        prev = 0
        for x in range(0, len(nums)):
            prev = runsum
            runsum = runsum + nums[x]
            nums[x] = nums[x] + prev
        return nums
