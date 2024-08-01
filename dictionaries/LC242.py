class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for ltr in t:
            if ltr not in dic.keys():
                dic[ltr] = 0
            dic[ltr] += 1
        
        for ltr in s:
            if ltr not in dic.keys():
                return False
            else:
                dic[ltr] -= 1
        
        for ltr in dic.keys():
            if dic[ltr] != 0:
                return False
        return True
                
'''
OR just 
return Counter(s) == Counter(t)
didn't know that shit
'''