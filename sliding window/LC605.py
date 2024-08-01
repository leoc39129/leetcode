class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        i = 1
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        count = 0
        while(i < len(flowerbed) - 1):
            count = sum(flowerbed[i-1:i+2])
            if count == 0:
                n -= 1
                flowerbed[i] = 1
                i += 1
            i += 1
        return n <= 0