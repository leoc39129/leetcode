class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Base Cases:
        if len(needle) > len(haystack):
            return -1

        if len(needle) == 1:
            return haystack.find(needle)

        n = len(needle)
        for idx in range(len(haystack) - len(needle) + 1):
            # Look for needle[0], we know how far ahead in haystack we have to look
            if haystack[idx] == needle[0]:
                if haystack[idx:idx+n] == needle:
                    return idx
            
        return -1
        