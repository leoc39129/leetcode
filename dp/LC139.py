class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = {}
        def chop(s):
            if s in memo:
                return memo[s]
            if s in wordDict:
                memo[s] = True
                return True
            for i in range(1, len(s)):
                if s[:i] in wordDict and chop(s[i:]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False
        return chop(s)

'''
RT: O()
Space: O()

Couldn't even get my previous memoization/recursive solution. Here's a discussion board
solution using DP:


class Solution:
    def wordBreak(self, s, wordDict):
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break
        
        return dp[-1]
'''