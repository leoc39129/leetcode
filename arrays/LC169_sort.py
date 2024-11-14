import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        # Base Case:
        if len(nums) == 1:
            return nums[0]

        freq = int(math.floor(len(nums)/2))

        num_map = {}

        for idx in range(len(nums)):
            if nums[idx] not in num_map:
                num_map[nums[idx]] = idx
                nums[idx] = 1
            else:
                nums[num_map[nums[idx]]] += 1
                if nums[num_map[nums[idx]]] > freq:
                    return nums[idx]

        return 0

'''
RT: O(n)
Space: O(n)

Revisited this problem and came up with the solution above. Couldn't figure out the O(n) RT, O(1) space
solution, which is listed below.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = majority = 0
        
        for n in nums:
            if majority == 0:
                res = n
            
            majority += 1 if n == res else -1
        
        return res


Original solution I came up with

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

'''
        