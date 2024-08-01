class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        spl = s.split()
        for x in range(0, len(spl)):
            spl[x] = spl[x][::-1]
        s = " ".join(spl)
        return s
        
        