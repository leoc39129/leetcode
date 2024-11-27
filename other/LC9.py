class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        lst = list(str(x))
        # print(lst)

        l, r = 0, len(lst)-1

        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1

        return True

        
'''
Easy one to end the day.
'''