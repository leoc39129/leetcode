class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        recx = {}
        recy = {}
        for i in range(len(s)):
            if(recx.get(s[i]) != recy.get(t[i])):
                return False
            else:
                recx[s[i]], recy[t[i]] = i,i
        return True
        