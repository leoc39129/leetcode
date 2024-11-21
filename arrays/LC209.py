class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        l, r = 0, 1
        cur_sum = nums[0]
        min_len = 100001
        
        while r <= len(nums):
            if cur_sum < target:
                if r < len(nums):
                    cur_sum += nums[r]
                r += 1
            else:
                # We might have a minimal length subarray
                if r - l < min_len:
                    min_len = r - l
                cur_sum -= nums[l]
                l += 1
                
        if min_len == 100001:
            return 0
        return min_len
                

'''
RT: O(n)
Space: O(1)

Optimal solution! Could be a littleeeeee bit cleaner, see this db solution

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start_idx = 0
        end_idx = 0
        res = float('inf')
        sum = 0
        
        while end_idx < len(nums):
            sum += nums[end_idx]
            while sum >= target:
                res = min(res, end_idx-start_idx+1)
                sum -= nums[start_idx]
                start_idx +=1
            end_idx +=1
        
        return 0 if res == float('inf') else res


Even faster than the above...

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        min_len = float('inf')
        current_res = 0
        for r in range(len(nums)):
            current_res += nums[r]
            while current_res >= target:
                min_len = min(min_len, r - l + 1)
                current_res = current_res - nums[l]
                l += 1
        return min_len if min_len != float('inf') else 0


The problem asks that you find an O(nlogn) solution once you've found an O(n)
solution. At first I thought nlogn, that means sorting! But order is critical
in this problem, so sorting is a horrible choice. Instead, create a prefix sum array,
and then use binary search on all n elements


from bisect import bisect_left

class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        
        # Step 1: Compute prefix sums
        prefix = [0] * (n + 1)  # prefix[0] = 0 for convenience
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        # Step 2: Use binary search to find the smallest subarray
        min_length = float('inf')
        
        for i in range(1, n + 1):
            # Find the smallest index j such that prefix[j] >= prefix[i - 1] + target
            target_sum = prefix[i - 1] + target
            j = bisect_left(prefix, target_sum)
            if j <= n:  # Ensure j is within bounds
                min_length = min(min_length, j - (i - 1))
        
        return min_length if min_length != float('inf') else 0


'''