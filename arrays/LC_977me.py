class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st = 0
        end = len(nums) - 1
        ret = []
        while st != end:
            if abs(nums[st]) >= abs(nums[end]):
                ret.append(nums[st]*nums[st])
                st += 1
            else:
                ret.append(nums[end] * nums[end])
                end -= 1
        ret.append(nums[st]*nums[st])
        return ret[::-1]
        