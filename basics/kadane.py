'''
Kadane's Algorithm is a dynamic programming approach used to find the maximum sum of a contiguous 
subarray in an array of integers (both positive and negative). It operates with a time complexity 
of O(n) and works by maintaining a running sum of the subarray (current_sum) and updating a 
max_sum whenever current_sum exceeds max_sum.

If current_sum is less than the element itself, restart current_sum at the element (this means starting a new subarray).
'''

def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum
