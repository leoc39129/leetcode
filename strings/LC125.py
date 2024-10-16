class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        filtered_chars = [char.lower() for char in s if char.isalnum()]
        l, r = 0, len(filtered_chars) - 1

        while l < len(filtered_chars):
            if filtered_chars[l] != filtered_chars[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
        
'''
Very obvious two pointer solution. 

Can also just use:

return filtered_chars == filtered_chars[::-1]
'''