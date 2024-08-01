class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        ret = []
        low = lower - 1
        nums.insert(0, low)
        nums.append(upper + 1)
        #print(nums)
        for x in range(len(nums) - 1):
            if nums[x + 1] - nums[x] <= 1:
                continue
            else:
                ret.append([nums[x] + 1, nums[x+1] - 1])
        return ret