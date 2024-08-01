class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []

        # Modify nums in place, visit the 1-indexed number as you go through array
        # Flip that number's sign (neg/pos); if you ever visit a number and it's negative already, it means it has been
        # Visited twice AKA add it to the results array

        # Solution in O(n) time and O(n) space is easy asf
        
        for i in range(n):
            if nums[abs(nums[i]) - 1] < 0:
                res.append(abs(nums[i]))
                #nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
                #print("hi")
                #res.append(i)
            else:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
            #print(nums)
        return res