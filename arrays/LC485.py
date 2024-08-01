class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        ldr = set()
        for num in nums:
            if num == 1:
                cur += 1
            else:
                ldr.add(cur)
                cur = 0
        ldr.add(cur) 
        return max(ldr)