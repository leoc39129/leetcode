class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Base Case:
        if len(strs) == 1:
            return strs[0]

        min_len = min(len(word) for word in strs)
        ret = 0
        flag = False

        for idx in range(min_len):
            ch = strs[0][idx]
            for word in range(1, len(strs)):
                if strs[word][idx] != ch:
                    flag = True
            if not flag:
                ret += 1
            else:
                break
        if ret == -1:
            return ""
        else:
            return strs[0][0:ret]
        
'''
RT: O(n*m), m=avg length of string
Space: O(1)

Straight up easy solvable problem. Base case, strategy, and optimization all good.

A similar approach with a different idea from the discussion board:

class Solution:
    def longestCommonPrefix(self, strs):
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                
                pref = pref[0:pref_len]
        
        return pref
'''