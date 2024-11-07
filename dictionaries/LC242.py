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

Came back to this problem, solved it very similarly!

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Base Case
        if len(s) != len(t):
            return False

        s_dict = {}
        for ch in s:
            if ch not in s_dict.keys():
                s_dict[ch] = 1
            else:
                s_dict[ch] += 1
                
        for ch in t:
            if ch not in s_dict.keys():
                return False
            else:
                s_dict[ch] -= 1

        for key in s_dict.keys():
            if s_dict[key] != 0:
                return False

        return True


        
'''