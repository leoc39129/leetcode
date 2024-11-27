class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = set()
        while n > 1 and n not in nums:
            nums.add(n)
            n_str = str(n)
            n = 0
            for digi in n_str:
                n += int(digi) * int(digi)
        if n == 1:
            return True
        else:
            return False
            