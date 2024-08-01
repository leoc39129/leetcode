class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(s) == 0:
            return 0
        count = 0
        idx = 0
        g.sort()
        s.sort()

        for num in g:
            while idx < len(s) and s[idx] < num:
                idx += 1
            if idx == len(s):
                return count
            count += 1
            s[idx] = 0
        return count