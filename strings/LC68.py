class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line_len = 0
        line_strs = []
        cur = []
        for idx in range(len(words)):
            if line_len+len(cur)+len(words[idx]) <= maxWidth:
                cur.append(words[idx])
                line_len += len(words[idx])
            else:
                cur.append(line_len)
                line_strs.append(cur)
                cur = [words[idx]]
                line_len = len(words[idx])
        cur.append(line_len)
        line_strs.append(cur)
        # We have each line ready, now join them with proper spacing
        for idx in range(len(line_strs)):
            line_len = line_strs[idx].pop()
            words = len(line_strs[idx])
            if idx == len(line_strs) - 1:
                # Left justified
                line_strs[idx] = " ".join(line_strs[idx])
                line_strs[idx] += " " * (maxWidth - len(line_strs[idx]))
            elif words > 1:
                whitespace = (maxWidth - line_len) / (len(line_strs[idx]) - 1)
                line_strs[idx] = self.setWhiteSpaces(line_strs[idx], line_len, maxWidth, words)
            else:
                # Single word
                line_strs[idx][0] += " " * (maxWidth - line_len)
                line_strs[idx] = line_strs[idx][0]
        return line_strs

    def setWhiteSpaces(self, line_strs, line_len, maxWidth, words):
        whitespaces = [0]*(len(line_strs)-1)
        total = 0
        idx = 0
        while total < maxWidth - line_len:
            whitespaces[idx] += 1
            total += 1
            idx += 1
            if idx > len(whitespaces)-1:
                idx = 0
        for idx in range(len(line_strs)-1):
            line_strs[idx] = line_strs[idx] + " "*whitespaces[idx]
        return "".join(line_strs)

            
            
'''
RT: O(n)
Space: O(n)

Went over 45 mins, but a solid solution. 

Here's a different approach but similar solution


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, line, width = [], [], 0

        for w in words:
            if width + len(w) + len(line) > maxWidth:
                for i in range(maxWidth - width): line[i % (len(line) - 1 or 1)] += ' '
                res, line, width = res + [''.join(line)], [], 0
            line += [w]
            width += len(w)

        return res + [' '.join(line).ljust(maxWidth)]
        

Here's GPT's optimal soln

class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        current_line = []  # Current line of words
        current_len = 0    # Total length of characters in the current line
        
        for word in words:
            # Check if adding the current word exceeds the line width
            if current_len + len(current_line) + len(word) > maxWidth:
                # Format the current line
                result.append(self.formatLine(current_line, current_len, maxWidth, last_line=False))
                current_line = []
                current_len = 0
            
            # Add the current word to the line
            current_line.append(word)
            current_len += len(word)
        
        # Add the final line, left-justified
        result.append(self.formatLine(current_line, current_len, maxWidth, last_line=True))
        
        return result
    
    def formatLine(self, line, line_len, maxWidth, last_line):
        """
        Format a line with proper justification.
        """
        if last_line or len(line) == 1:
            # Left-justify: Join words with a single space and pad the end
            return " ".join(line).ljust(maxWidth)
        
        # Distribute spaces evenly
        total_spaces = maxWidth - line_len
        space_between = total_spaces // (len(line) - 1)  # Minimum spaces between words
        extra_spaces = total_spaces % (len(line) - 1)   # Distribute leftover spaces
        
        # Add spaces between words
        justified_line = ""
        for i in range(len(line) - 1):
            justified_line += line[i]
            justified_line += " " * (space_between + (1 if i < extra_spaces else 0))
        
        justified_line += line[-1]  # Add the last word
        return justified_line

'''