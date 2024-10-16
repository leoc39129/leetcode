class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return int(s[0])

        stack = []
        stack_len = 0
        idx = 0

        print(s)

        while idx < len(s):
            print(stack)
            if s[idx] == " ":
                idx += 1
            else:
                if s[idx] == "(":
                    counter = 1
                    temp = idx + 1

                    while counter != 0:
                        if s[temp] == ")":
                            counter -= 1
                        elif s[temp] == "(":
                            counter += 1
                        temp += 1
                    stack.append(self.calculate(s[idx + 1: temp - 1]))
                    idx = temp
                    stack_len += 1
                elif s[idx] == "+" or s[idx] == "-":
                    stack.append(s[idx])
                    stack_len += 1
                    idx += 1
                else:
                    temp = idx + 1
                    while temp < len(s):
                        try:
                            val = int(s[temp])
                            temp += 1
                        except ValueError:
                            break
                        
                    stack.append(s[idx:temp])
                    idx = temp
                    stack_len += 1

                if stack_len > 2:
                    val1 = stack.pop()
                    op = stack.pop()
                    val2 = stack.pop()

                    if op == "+":
                        stack.append(str(int(val1) + int(val2)))
                    elif op == "-":
                        stack.append(str(int(val2) - int(val1)))

                    stack_len -= 2


        return int(stack.pop())


'''
Didn't have enough time to figure out "-(2+3-4)" or "-1" type expressions ("-" used as a unary)

Here's two discussion board solutions. Looks like everyone uses the same type of solution

class Solution:
    def calculate(self, s: str) -> int:
        number = 0
        sign_value = 1
        result = 0
        operations_stack = []

        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c in "+-":
                result += number * sign_value
                sign_value = -1 if c == '-' else 1
                number = 0
            elif c == '(':
                operations_stack.append(result)
                operations_stack.append(sign_value)
                result = 0
                sign_value = 1
            elif c == ')':
                result += sign_value * number
                result *= operations_stack.pop()
                result += operations_stack.pop()
                number = 0

        return result + number * sign_value

        

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_res,curr_num = 0,0
        sign = 1
        for i in range(len(s)):

            char = s[i]

            if char.isdigit():
                curr_num = curr_num*10+int(char)

            elif char == '+' or char == '-':
                curr_res += curr_num*sign
                sign = 1 if char == '+' else -1
                curr_num = 0

            elif char == '(':
                stack.append((curr_res, sign))
                curr_res = 0
                sign = 1

            elif char == ')':
                curr_res+=sign*curr_num
                prev, p_sign = stack.pop()
                curr_res = prev+curr_res*p_sign
                curr_num = 0

        curr_res += curr_num*sign
        return curr_res

            
'''