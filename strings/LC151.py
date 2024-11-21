import re

class RegexSolution1(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Base Case
        if len(s) == 1:
            return s

        s = s.strip()
        s = re.sub(r'\s+', ' ', s)
        
        start = len(s)-1
        end = len(s)-1

        lst = []
        for idx in range(len(s)-1, -1, -1):
            if s[idx] == " ":
                lst.append(s[end+1:start+1])
                end = idx - 1
                start = idx - 1
            else:
                end -= 1
        lst.append(s[0:start+1])
        return ' '.join(lst)


class RegexSolution2(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Base Case
        if len(s) == 1:
            return s

        s = s.strip()
        s = re.sub(r'\s+', ' ', s)
        
        start = 0
        end = 0

        lst = list(s)
        for idx in range(len(s)):
            if lst[idx] == " " or idx == len(s)-1:
                if idx == len(s)-1:
                    r = end
                else:
                    r = end-1
                l = start
                while l < r:
                    lst[l], lst[r] = lst[r], lst[l]
                    l += 1
                    r -= 1
                start = end + 1
            end += 1
        
        lst.reverse()
        #print(lst)
        return ''.join(lst)

class NoRegexAttempt(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Base Case
        if len(s) == 1:
            return s

        s = s.strip()
        
        start = 0
        end = 0

        lst = list(s)
        lst.reverse()
        print(lst)
        for idx in range(len(lst)):
            if lst[idx] == " " and lst[idx-1] == " ":
                continue
            elif idx == len(lst)-1 or lst[idx] == " ":
                if idx == len(lst)-1:
                    r = end
                else:
                    r = end-1
                l = start
                while l < r:
                    lst[l], lst[r] = lst[r], lst[l]
                    l += 1
                    r -= 1
                # Get through double spaces
                while end < len(lst) and lst[end] == ' ':
                    end += 1
                    print('HAI')
                start = end
            else:
                end += 1

        print(lst)
        return ''.join(lst)

'''
Good job realizing the pattern early.

Didn't realize that skipping the extra whitespaces in the list doesn't solve the problem,
they're still in the list -- using RegexSolution1's approach of adding words to a new list
would've been better and worked in the NoRegexAttempt. Here's GPT's (very slow) correction of this issue

class GPTSolution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Base Case
        if len(s) <= 1:
            return s.strip()

        # Trim leading and trailing spaces
        s = s.strip()

        # Reverse the entire string
        lst = list(s)
        lst.reverse()

        start = 0  # Start of the current word
        end = 0    # End of the current word

        # Reverse each word in the reversed list
        while end < len(lst):
            if lst[end] == " ":
                # Reverse the current word
                self.reverse(lst, start, end - 1)
                # Skip through multiple spaces
                while end < len(lst) and lst[end] == " ":
                    end += 1
                start = end
            else:
                end += 1

        # Reverse the last word (if any)
        self.reverse(lst, start, len(lst) - 1)

        # Remove extra spaces in between
        return ''.join(lst)

    def reverse(self, lst, l, r):
        """Helper to reverse a sublist in-place."""
        while l < r:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1

    def removeExtraSpaces(self, lst):
        """Helper to remove extra spaces between words."""
        result = []
        for i, char in enumerate(lst):
            if char == " " and (not result or result[-1] == " "):
                continue  # Skip multiple spaces
            result.append(char)
        return result
'''
        
        
        
        
        