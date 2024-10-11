class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Base Case:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        elif len(s) == 2:
            if s[0] != s[1]:
                return 2
            else:
                return 1

        # Sliding Window
        # You need a way to keep track of the characters you've seen in the current substring
        
        l, r = 0, 1
        tracker = [s[0]]
        counter = 1
        cur_max = 0

        while r < len(s):
            if s[r] not in tracker:
                tracker.append(s[r])
                counter += 1
                
                r += 1
            else:
                if counter > cur_max:
                    cur_max = counter
                while s[l] != s[r]:
                    tracker.remove(s[l])
                    l += 1
                r += 1
                l += 1
                counter = r - l
        if counter > cur_max:
            cur_max = counter
        return cur_max


'''
Good job! Done in 20 mins 

Discussion Board Solution using a Set instead of the array

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength
'''