class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        dic = {}
        ans = []
        for arr in nums:
            for x in arr:
                if x not in dic.keys():
                    dic[x] = 1
                else:
                    dic[x] += 1
        for key, value in dic.items():
            if value == len(nums):
                ans.append(key)
        return sorted(ans)
        
        