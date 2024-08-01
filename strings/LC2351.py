class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        ltrs = set()
        for char in s:
            if char in ltrs:
                return char
            else:
                ltrs.add(char)
