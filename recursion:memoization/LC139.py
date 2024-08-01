class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Doesn't work with huge inputs
        # How does the dictionary help? What examples do we reuse words?
        def chop(s, wordDict):
            if len(s) == 0:
                return True
            for wrd in wordDict:
                dum = s.find(wrd)
                if dum != -1:
                    ln = len(wrd)
                    if chop(s[dum + ln:], wordDict) and chop(s[:dum], wordDict):
                        return True
            return False

        return chop(s, wordDict)
        '''
        # ChatGPT ftw
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
In this implementation, the function chop uses memoization to store the result of a given string s in a dictionary memo. This way, if the same string s is encountered again, the result can be quickly looked up in the memo dictionary, instead of having to recompute it. This greatly reduces the number of redundant computations and improves the overall time complexity.





        '''