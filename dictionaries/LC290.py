class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # Base Case:
        if len(pattern) > len(s):
            return False

        s_list = s.split(' ')

        if len(pattern) != len(s_list):
            return False

        pattern_dict = {}
        idx = 0
        for ch in pattern:
            if ch not in pattern_dict.keys():
                pattern_dict[ch] = s_list[idx]
            else:
                if pattern_dict[ch] != s_list[idx]:
                    return False

            idx += 1

        key_set = set(pattern_dict.keys())
        val_set = set(pattern_dict.values())

        if len(key_set) != len(val_set):
            return False

        return True

'''
RT: O(n)
Space: O(n)

Optimal solution and very straight forward. Good job
'''