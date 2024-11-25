def main():
    s = "({[]})"

    opening = "({["
    closing = ")}]"

    translate = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    stack = []
    '''
    General idea: Add all open parentheses to the stack, when you encounter a closed parentheses, its corresponding open parenthesis should
    be the most recently appended to the stack (If not, your input would be invalid, such as "( [ { ] } )"). Thus, to make sure the
    corresponding, correct parenthesis is at the end of the stack, get the open version of the current char via the dictionary, make sure
    that it's equal to the last char on the stack. If it is, pop the stack (get rid o' last char on the stack), move on. If not, return False
    '''
    

    for char in s:
        if char in opening:
            stack.append(char)
        if char in closing:
            if stack and translate.get(char) == stack[-1]:  
                stack.pop()
            else:
                return False

    if not stack:
        return True
    else: 
        return False
    '''
    if stack:
        print("Hello world!")
    if not stack:
        print("not Hello world!")
    '''
    



if __name__ == "__main__":
    main()


'''
Came back to this one, wow my code was not the greatest whenever I did this one.
Here's what I came up with in ~5 mins

RT: O(n)
Space: O(n)

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1 or s[0] in ']})':
            return False

        openclose = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

        stack = []
        idx = 0
        while idx < len(s):
            if s[idx] in "[{(":
                stack.append(s[idx])
            elif stack:
                elem = stack.pop()
                if openclose[elem] != s[idx]:
                    return False
            else:
                return False

            idx += 1
        
        return not stack
        