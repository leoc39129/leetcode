'''
Inefficient first solution O(nlogn)

So you were right, the max hIndex is len(citations)... DUH!

Good catch on the sorting, just a blunder not realizing the easy ways to do this
VISUALIZE next time!

Come back to this problem, see if you can get the O(n) RT, O(n) space solution below

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        temp = [0 for _ in range(n + 1)]

        for i,v in enumerate(citations):
            if v > n :
                temp[n] += 1
            else:
                temp[v] += 1
        
        total = 0
        for i in range(n, -1, -1):
            total += temp[i]
            if total >= i:
                return i

'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        ret = 0
        citations.sort()


        counts = [0]*(citations[-1] + 1)

        for c in citations:
            for num in range(c+1):
                counts[num] += 1
        
        
        idx = 0
        while idx < len(counts) and counts[idx] >= idx:
            ret = idx
            idx += 1
        return ret
        
        
