class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Base Case
        if len(s) > len(t):
            return False
        
        if not s:
            return True

        s_idx = 0
        t_idx = 0

        while t_idx < len(t) and s_idx < len(s):
            if t[t_idx] == s[s_idx]:
                s_idx += 1
            t_idx += 1

        if s_idx == len(s):
            return True
        return False


'''
RT: O(n)
Space: O(1)

Nice and easy
'''