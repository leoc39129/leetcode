class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Base Cases: If the array is of length zero or one
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1

        # Sliding window approach, look at idx l and r, advance until we get
        # nums[l] == val, hold l in place. Then advance idx r until it finds
        # a nums[r] != val. Swap em! 

        # Every time idx l is incremented, increment counter k

        k = 0
        l = 0
        r = 1

        # Four situations
        # 1. nums[l] == val and nums[r] != val -> Swap and increment l, r, k
        # 2. nums[l] == val and nums[r] == val -> Increment r
        # 3. nums[l] != val and nums[r] != val -> Increment l, r, k
        # 4. nums[l] != val and nums[r] == val -> Increment l, r, k
        
        while r < len(nums):
            if nums[l] == val and nums[r] != val:
                temp = nums[r]
                nums[r] = val
                nums[l] = temp
                r += 1
                l += 1
                k += 1
            elif nums[l] == val and nums[r] == val:
                r += 1
            else:
                l += 1
                r += 1
                k += 1

        # If the array has all nums[i] != val, then we'll forget about the last
        # element of the array due to the double pointer/sliding window approach
        # As a result, look at nums[l] at the end and increment k accordingly
        
        if nums[l] != val:
            k += 1

        # Return k
        return k
        
        '''
        Simpler solution:
        # The basic idea: Fill the first k elements of the array with the 
        # nums[i] != val, where k represents the number of elements in the array
        # that do not equal val. This is technically a two ptr approach, but
        # really simplifies down to a one ptr approach as the code really just
        # goes through nums one time (RT: O(n)) and tracks where the next nums[i]
        # that doesn't equal val should be placed.

        # Easily visualize this by running through an example
        # val = 3, nums = [3, 2, 2, 3, 3]

        # Plus, no base cases to deal with
        
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        
        return idx
        '''