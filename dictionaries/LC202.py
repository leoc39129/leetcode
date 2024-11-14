class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set([n])

        str_n = str(n)
        total = 0
        while True:
            total = 0
            for dig in str_n:
                total += int(dig)*int(dig)
            if total == 1:
                return True
            elif total in seen:
                return False
            else:
                seen.add(total)
                str_n = str(total)

'''
Well done! A little bit inefficient due to string iteration/conversion, but it's got a good runtime and space baseline

Here's a discussion board solution:

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result_set = set()
        while n != 1:
            if n not in result_set:
                result_set.add(n)
                total = 0
                while n != 0:
                    total += (n % 10) ** 2
                    n = n // 10
                n = total
            else: #n is in result_set, a loop is found
                return False
        return True

'''

                

        

        