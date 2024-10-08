#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    stk = []
    for ch in s:
        if len(stk) == 0:
            stk.append(ch)
        elif ch == stk[-1]:
            stk.pop()
        else:
            stk.append(ch)
    if len(stk) == 0:
        return "Empty String"
    else:
        return "".join(stk)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
