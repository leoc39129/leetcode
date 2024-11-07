class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        conversion = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        last = 1001
        total = 0

        for ch in s:
            num = conversion[ch]
            if num > last:
                total -= last
                total += num - last
            else:
                total += num
            last = num

        return total


'''
Straightforward solution, well done.

An interesting alternate approach, looking at two characters at once

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                res -= roman[a]
            else:
                res += roman[a]

        return res + roman[s[-1]] 
'''