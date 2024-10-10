class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # Base Case: None, we will always have len(tokens) > 0

        stack = []

        # Find the first operator, that is the innermost expression
        front = 0

        for idx in range(1, len(tokens) + 1):
            try:
                val = int(tokens[-idx])
                keeper = idx
            except ValueError:
                try:
                    # Operator on the end with a number to its left
                    val = int(tokens[-idx - 1])
                    stack.append(val)
                    stack.append(tokens[-idx])
                    idx += 1
                except ValueError:
                    # Operator on the end with an operator to its left
                    # Make sure we maintain order for - and /

                    if tokens[-idx] == "*" or tokens[-idx] == "+":
                        stack.append(int(tokens[front]))
                        front += 1
                        stack.append(tokens[-idx])
                    else:
                        stack.append(tokens[-idx])
                        stack.append(int(tokens[front]))
                        front += 1

        print(stack)
        ret = int(tokens[-keeper+front])
        print(ret)

        while(len(stack) > 0):
            val = stack.pop()
            try:
                val = int(val)
                op = stack.pop()
                if op == u'/':
                    if val < 0 or ret < 0:
                        ret = (val // ret) + 1
                    else:
                        ret = val // ret
                elif op == u'-':
                    ret = val - ret

            except ValueError:
                if val == u'*':
                    ret = ret * stack.pop()
                elif val == u'+':
                    ret = ret + stack.pop()
                elif val == u'/':
                    ret = ret // stack.pop()
                elif val == u'-':
                    ret = ret - stack.pop()
            print(ret)
        return ret

'''
How do we build this stack?
Ex1: ["2","1","+","3","*"] --> [+,1,*,3] --> [3,*,1,+]
Ex2: ["4","13","5","/","+"] --> [/,5,+,4] --> [4,+,5,/]
Ex3: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] -->
     [5,+,17,+,10,*,/,6,-11,*,3,+]

Order only matters for / and - . So in our stack if we want 6 divided by what
came before, signal that by putting the number first. Same with subtraction.
Otherwise, it should be operator then number
'''

'''
Using someone else's solution...

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for st in tokens:
            if st == '+':
                stack.append(stack.pop() + stack.pop())
            elif st == '*':
                stack.append(stack.pop() * stack.pop())
            elif st == '-':
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif st == '/':
                second, first = stack.pop(), stack.pop()
                result = first // second
                if result < 0 and first % second != 0:
                    result += 1
                stack.append(result)
            else:
                stack.append(int(st))
        #print(stack)

        ret = stack.pop()
        return ret


COME BACK TO THIS PROBLEM:
What did we learn...
1. You don't have to make the entire stack and then use it. In this case, it was way better to use it as you go.
2. This code started to get WAY too complicated for a LeetCode medium. That should've been a warning sign -- be wary 
   for that in the future, and be open to rethinking your approach
3. 
'''
        