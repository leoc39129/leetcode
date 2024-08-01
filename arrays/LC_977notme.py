class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st = 0
        end = len(nums) - 1
        ret = [0 for x in range(len(nums))]

        i = end
        while i >= 0:
            if abs(nums[st]) >= abs(nums[end]):
                ret[i] = nums[st] * nums[st]
                st += 1
            else:
                ret[i] = nums[end] * nums[end]
                end -= 1
            i -= 1
        return ret