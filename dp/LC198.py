class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Base Case:
        # nums will always have one number...
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        if n == 4:
            return max(nums[0]+nums[3], nums[0]+nums[2], nums[1]+nums[3])

        ret = 0
        dp = [[0]*n for _ in range(2)]
        dp[0][0] = nums[0]

        for idx in range(1, n):
            dp[0][idx] = nums[idx] + max(dp[0][idx-2], dp[1][idx-2])
            dp[1][idx] = max(dp[0][idx-1], dp[1][idx-1])

        print(dp)
        ret = max(dp[0][n - 1], dp[1][n - 1])
        return ret


'''
The thing is, you don't need to use space, much less O(n) space (or O(2n) space)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        memo = [0 for _ in range(len(nums) + 1)]
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            memo[i+1] = max(memo[i], memo[i-1] + val)

        return memo[len(nums)]

    
From this solution, notice how you only need memo[i] and memo[i-1]. Why use an array
when you can just use two variables? From that insight...


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        prev1 = 0
        prev2 = 0
        
        for num in nums:
            tmp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = tmp

        return prev1
    

        
'''