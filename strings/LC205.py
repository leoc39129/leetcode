class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 1:
            return True

        letter_map = {}
        t_set = set()

        for idx in range(len(s)):
            if s[idx] not in letter_map:
                if t[idx] in t_set:
                    return False
                else:
                    letter_map[s[idx]] = t[idx]
                    t_set.add(t[idx])
            else:
                if letter_map[s[idx]] != t[idx]:
                    return False

        return True
        

'''
RT: O(n)
Space: O(1)

Nailed it
'''