class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Base Case:
        m = len(s)
        n = len(t)
        if n > m:
            return ""
        
        t_dict = {}
        for ch in t:
            if ch not in t_dict.keys():
                t_dict[ch] = 1
            else:
                t_dict[ch] += 1

        l, r = 0, 0
        s_dict = {}
        incr = True

        ret = ""
        ret_len = 1000000


        while r < m:
            print(s[l:r+1])
            if incr:
                # If we incremented r, add it to s_dict
                if s[r] not in s_dict.keys():
                    s_dict[s[r]] = 1
                else:
                    s_dict[s[r]] += 1
                incr = False

            for key in t_dict.keys():
                if key not in s_dict.keys() or s_dict[key] != t_dict[key]:
                    incr = True
            if incr:
                r += 1
            else:
                # We've found a substring, let's see if we can minimize the window
                while s[l] not in t_dict.keys():
                    s_dict[s[l]] -= 1
                    l += 1
                if r - l < ret_len:
                    ret = s[l:r+1]
                    ret_len = len(ret)

                while l < r:
                    s_dict[s[l]] -= 1
                    l += 1

                r = l
                
        return ret
    
'''
Almost got it -- in the "We've found a substring" part, you forgot that you have to find the
second character from t and restart from there, not just go to the end of the substring and
assume that was the minimum.

Example:
s = "bdab"
t = "ab"

Window progression currently:

b
bd
bda
b

it should be:

b
bd
bda
a
ab

Here's a slightly confusing discussion board solution

Instead of the dictionary, the array initially stores the frequencies of all of the characters in t
As it iterates through s, it decrements map[ord(ch)] NO MATTER WHAT, so that characters in s that
are not in will go into the negative numbers. The count variable is used to track how many characters
from t still need to be encountered in s to form a substring. This is why the inner while loop
(while count == 0) is used to denote when a substring has been found. The if map[ord(s[start])] == 0:
means that a character from t has been found (as characters in s not in t will have negative values),
and we need to stop minimizing the window by incrementing start, and we need to start increasing the 
window length to try and find that character again later in string s.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        map = [0] * 128
        count = len(t)
        start = 0
        end = 0
        min_len = float('inf')
        start_index = 0
        # UPVOTE !
        for char in t:
            map[ord(char)] += 1

        while end < len(s):
            if map[ord(s[end])] > 0:
                count -= 1
            map[ord(s[end])] -= 1
            end += 1

            while count == 0:
                if end - start < min_len:
                    start_index = start
                    min_len = end - start

                if map[ord(s[start])] == 0:
                    count += 1
                map[ord(s[start])] += 1
                start += 1

        return "" if min_len == float('inf') else s[start_index:start_index + min_len]
'''