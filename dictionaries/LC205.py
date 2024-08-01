class Solution(object):    
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        transl = {}
        for x in range(len(s)):
            
            if s[x] not in transl.keys():
                if t[x] not in transl.values():
                    transl[s[x]] = t[x]
                else:
                    return False
                
            elif t[x] != transl[s[x]]:
                return False
        return True
        
        
        