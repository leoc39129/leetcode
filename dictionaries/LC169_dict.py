class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydict = {}
        for x in nums:
            if x not in mydict.keys():
                mydict[x] = 1
            else:
                mydict[x] += 1
        n = len(nums)
        for key, value in mydict.items():
            if value > n / 2:
                return key
        