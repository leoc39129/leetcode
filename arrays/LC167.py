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