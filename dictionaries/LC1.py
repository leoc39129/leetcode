class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for k in range(len(nums)):
            if target-nums[k] not in dict:
                dict[nums[k]] = k
            else:
                return [dict[target-nums[k]], k]
            

