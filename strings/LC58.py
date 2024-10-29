# Initial useful solution

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Base Case:
        if len(s) == 1:
            return 1

        words = []
        start = 0
        end = 0
        idx = 0
        word = False
        for ch in s:
            print(ch)
            print(word)
            print()
            if ch != " " and word:
                end += 1
            elif ch != " " and not word:
                start = idx
                end = idx
                word = True
            elif ch == " " and word:
                # We got a word!
                words.append(s[start:end+1])
                word = False

            idx += 1
        if s[len(s)-1] != " ":
            words.append(s[start:end+1])
        
        print(words)

        return len(words[-1])



        