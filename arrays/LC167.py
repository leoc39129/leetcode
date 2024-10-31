class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # sliding window!
        lft = 0
        right = len(numbers) - 1
        while(lft < right):
            if numbers[lft] + numbers[right] == target:
                return [lft+1, right+1]
            elif numbers[lft] + numbers[right] < target:
                lft += 1
            else:
                right -= 1

'''
Came back to this problem a while later, came up with a similar solution,
a little more specific due to the constraints of the problem

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Base Case:
        if len(numbers) == 2:
            return [1,2]

        l = 0
        r = len(numbers) - 1
        cur = -1001

        while cur != target:
            cur = numbers[l] + numbers[r]
            if cur == target:
                return [l+1, r+1]
            elif cur < target:
                l += 1
            else:
                # cur > target
                r -= 1
            

'''