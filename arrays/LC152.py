class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = -11
        prod1, prod2 = 1, 1
        size = len(nums)

        for i in range(0, size):
            j = size - i - 1
            prod1 *= nums[i]
            max_prod = max(prod1, max_prod)
            if prod1 == 0:
                prod1 = 1
            prod2 *= nums[j]
            max_prod = max(prod2, max_prod)
            if prod2 == 0:
                prod2 = 1
        return max_prod
        
        
'''
You have to go from the right and the left and simply update the maximum product you've seen
so far as you go. Say you have n negative numbers in the array --
(this is for the case that there are an odd amount of negative numbers) Going
from both the left and the right will ensure that you look at both subarrays where you have n-1
negative numbers, creating a positive product. Zeroes simply reset the cycle by setting prod1 or prod2
to one, where they will "catch" the next element to keep looking for a max product.

Another important concept from this is you don't always need to move the index you're looking at around,
you can take a shortcut here by resetting the product to 1.

Old Attempt:

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Base Case:
        if len(nums) == 1:
            return nums[0]

        # Sliding window? Start with the first element, extend until you hit a negative
        # number, which will be the "reset" on the window -- reslide until you find
        # another negative number

        # The question is what happens if you don't find another, like in 
        # [2,3,-2,4] or [2,3,-2,8] -- we need to be able to pick out
        # [2,3] and [8] respectively from these two different cases

        # We actually don't need a sliding window -- just the product
        # Iterate over the array, go until there's a sign change, store that as the 
        # max, keep going
        temp_max = 0
        prod = nums[0]
        for i in range(1, len(nums)):
            print(i)
            if (prod < 0 and nums[i] < 0) or (prod > 0 and nums[i] > 0):
                prod = prod * nums[i]
                if prod > temp_max:
                    temp_max = prod 
            elif (prod < 0 and nums[i] > 0) or (prod > 0 and nums[i] < 0):
                if prod > temp_max:
                    temp_max = prod
                prod = nums[i]
            elif nums[i] == 0:
                if prod > temp_max:
                    temp_max = prod 
                prod = 1
            print(temp_max)
            print(prod)

        return temp_max
'''