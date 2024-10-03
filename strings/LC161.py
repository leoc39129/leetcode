class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # s_dict = {}
        # for ch in s:
        #     if ch is not in s_dict.keys():
        #         s_dict[ch] = 1
        #     else:
        #         s_dict[ch] += 1

        # Order matters: Dictionary approach won't work

        # Linked lists?

        # Cases:
        # 1. "ab" vs. "abc": One character extra, otherwise the same string
        #    an insert or delete will work here
        # 2. "ab" vs. "ab": The exact same word, return FALSE
        # 3. "abz" vs. "abc": Same number of characters, with two different ones
        #    ONLY a replacement will work here, still return True

        # Substring problem? "ab" is in "abc"

        ret = False

        if abs(len(s) - len(t)) > 1:
            return False

        if (len(t) == 0 and len(s) == 1) or (len(s) == 0 and len(t) == 1):
            return True

        # Now we know these strings have either equal lengths, or 
        # have lengths that differ by 1

        if len(s) == len(t):
            # We have to replace a character if this is going to work
            diff = 0
            for idx in range(len(s)):
                if s[idx] != t[idx]:
                    diff += 1
            
            if diff == 1:
                ret = True

        else:
            # We need to insert or delete one character

            # Instead of tallying differences like we do for when s and t have 
            # the same length, once we find a difference we either need to skip
            # an index in string s, or skip an index in string t -- if we find
            # another difference, the two strings are more than one edit distance
            # apart, i.e. return False

            # s = "acb", t = "ab" vs. s = "ab", t = "acb"

            if len(s) > len(t):
                # Skip an idx on s (deletion)

                t_decr = 0
                for idx in range(len(s)):
                    print(idx)
                    print(idx - t_decr)
                    if (idx + t_decr == len(t)) or (s[idx] != t[idx + t_decr]):
                        t_decr -= 1

                if t_decr == -1:
                    ret = True
            else:
                # Skip an idx on t (insertion)
                s_decr = 0
                for idx in range(len(t)):
                    if (idx + s_decr == len(s)) or (t[idx] != s[idx + s_decr]):
                        s_decr -= 1

                if s_decr == -1:
                    ret = True
        
        return ret

'''
It may look complicated, but it's still an O(N) time complexity and O(1) space complexity
'''