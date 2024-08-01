class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Started out with the sliding window/two pointer approach -- define four
        cases (think truth table), act accordingly! It's too slow...

        So, you have to switch to a smarter approach -- two pointers, but one tracks
        non zero numbers, the other tracks zeroes! Basically, the idea is...

        1. If the zero ptr isn't pointing to zero, advance it

        2. If we do have the zero ptr pointing to a zero, we may need to swap
        but only swap if the nonzero ptr is pointing somewhere ahead in the array
        AND if that ptr is pointing to a nonzero number

        3. Otherwise, advance nonzero pointer. This will happen when the nonzero
        pointer is pointing to the same number as the zero pointer (aka zero == non)
        OR when there are two zeroes in a row, but zero != non

        Didn't get it very quickly but I think this would've worked for me in 
        an interview setting. Went through a failing approach, pivoted, succeeded!
        """
        
        if len(nums) < 2:
            return nums
        
        non = 0
        zero = 0

        while zero < len(nums) and non < len(nums):
            if nums[zero] != 0:
                zero += 1
            elif non > zero and nums[non] != 0:
                nums[zero] = nums[non]
                nums[non] = 0
                non += 1
            else:
                non += 1
            


