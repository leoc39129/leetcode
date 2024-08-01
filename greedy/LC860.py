class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills[0] != 5:
            return False
        change = {10:0, 5:0}
        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if change[5]:
                    change[10] += 1
                    change[5] -= 1
                else:
                    return False
            else:
                # We have a $20
                if change[10] and change[5]:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False

        return True

        # O(N) solution with dictionary

        