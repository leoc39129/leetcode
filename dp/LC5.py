class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 1:
            return s

        dp = [[False]*n for _ in range(n)]

        max_row = 0
        max_col = 0
        max_len = 1

        for col in range(n):
            dp[col][col] = True
            for row in range(col):
                if s[row] == s[col] and (col-row <= 2 or dp[row+1][col-1]):
                    dp[row][col] = True
                    if col-row > max_len-1:
                        max_len = col-row+1
                        max_row = row
                        max_col = col

        return s[max_row:max_col+1]
                
        
'''
RT: O(n^2)
Space: O(n^2)

Almost got the full dp solution, not quite right. Had the right concept, but the key was
you only have to check if current string minus the ends is a palindrome after checking for
s[i] == s[j], not every single iteration down. But, there's an even better way to do this called
Manacher's Algorithm

class Solution:
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            if i+dp[i] > right:
                center = i
                right = i+dp[i]
            if dp[i] > Max_Len:
                Max_Len = dp[i]
                Max_Str = s[i-dp[i]:i+dp[i]+1].replace('#','')
        return Max_Str
'''