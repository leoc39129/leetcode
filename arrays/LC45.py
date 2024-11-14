class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Base Case:
        if n == 1:
            return 0

        if nums[0] >= n - 1:
            return 1

        jumps = 0
        for idx in range(len(nums)):
            jump_len = nums[idx]
            # Can we jump to the end
            if idx + jump_len >= n-1:
                return jumps+1
            for i in range(idx, idx+jump_len):


'''
This problem rocked me. Tried a bunch of different stuff, as I do remember doing
Jump Game I, but that was totally not the right approach. I had the right idea at the end,
in checking what's the farthest you can jump to in the range of your current index, but
didn't pull the trigger and implement. On to the next.

Here's a db soln

class Solution:
    def jump(self, nums):
        near = far = jumps = 0

        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            
            near = far + 1
            far = farthest
            jumps += 1
        
        return jumps

Here's GPT's solution

class Solution:
    def jump(self, nums):
        jumps = 0          # Number of jumps needed
        max_reach = 0      # Farthest we can reach with current jump
        edge = 0           # End of the range we can reach with the current jump

        for i in range(len(nums) - 1):  # No need to jump from the last element
            max_reach = max(max_reach, i + nums[i])  # Update max reach

            if i == edge:  # Time to make a jump to go further
                jumps += 1
                edge = max_reach  # Update the edge to max reach

        return jumps

'''