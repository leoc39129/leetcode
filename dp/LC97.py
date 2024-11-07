class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # Base Case:
        if len(s1) + len(s2) != len(s3):
            return False
        
        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True
        
        if len(s3) == 0 and (len(s1) != 0 or len(s2) != 0):
            return False

        if len(s2) == 0:
            if s1 == s3:
                return True
            else:
                return False

        if len(s1) == 0:
            if s2 == s3:
                return True
            else:
                return False

        matrix = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
        
        for idx in range(1, len(s1+1)):
            matrix[0][idx] = matrix[0][idx-1] + s1
        
        return True
    
'''
Very confusing one. I had a general idea but I came up with it far too late to implement. Learn from
this one and move on. Here's a discussion board solution with an explanation:


Instead of using integers in the matrix, use T/F! It makes a lot of intuitive sense -- first, fill
out the first row and column seeing how "far" you can get in s1 and s2 and match s3. Next, loop
through the "inner" part of the array, looking at the index above and to the left to see if the
current index is a possible path (or, the current index = True). 

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[m][n]


Here's the 1D approach:

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        
        if m < n:
            return self.isInterleave(s2, s1, s3)
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[n]
'''