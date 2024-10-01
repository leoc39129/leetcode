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