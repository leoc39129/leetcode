class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        dic[0] = 1
        ret = pref = 0
        for num in nums:
            pref += num
            if pref not in dic.keys():
                dic[pref] = 1
            else:
                dic[pref] += 1
            if pref - k in dic.keys():
                ret += dic[pref-k]
        return ret