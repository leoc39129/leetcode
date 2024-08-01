class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                s = i*i + j*j
                cur = math.floor(sqrt(s))
                if(cur <= n and s == cur*cur):
                    count += 2
        return count
