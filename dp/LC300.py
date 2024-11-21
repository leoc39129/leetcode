class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1

        dp = [[0]*len(nums) for _ in range(len(nums))]
        dp_max = -1
        for row in range(len(nums)):
            last = row
            for col in range(row, len(nums)):
                if row == col:
                    dp[row][col] = 1
                elif nums[col] < nums[row]:
                    dp[row][col] = 1
                elif nums[col] > nums[row]:
                    if nums[col] >= nums[last]:
                        dp[row][col] = dp[row][last] + 1
                        last = col
                    else:
                        dp[row][col] = dp[row][last]
                    
            dp_max = max(dp_max, dp[row][len(nums)-1])

        print(dp)
        return dp_max


'''
I felt like I was on the right path and close to a solution but I had my framework wrong.
Instead of looking at it as where should the Longest Increasing Subsequence (LIS) start,
it should be viewed as where does the LIS end. See the discussion board solution below, where 
there's a double for loop and the nested for loop loops from 0 --> i, the outer for loop's value.
So it goes 0->0, 0->1, 0->2, ...

class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
            #print(dp)
        return max(dp)


But, there's an even better approach. Greedy and binary search!

Essentially, you keep the sub array sorted, by adding any number that's greater than the last
number in the array to the end, while using binary search to replace the smallest element in sub
that's greater than or equal to the current element.

For example: [2, 6, 8, 3, 4, 5, 1]
Iter# : sub
    0 : [2]
    1 : [2,6]
    2 : [2,6,8]
    3 : [2,3,8]
    4 : [2,3,4]
    5 : [2,3,4,5]
    6 : [1,3,4,5]


class Solution:  # 68 ms, faster than 93.92%
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)


Here's the official Python documentation on bisect_left, I've summarized the important parts
bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)

Locate the insertion point for x in a to maintain sorted order in the already sortedlist a you give the function.
The return value is suitable for use as the first parameter to list.insert() assuming that a is already sorted.

Here, instead of using .insert, we replace sub[idx]
'''