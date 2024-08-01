class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur = -100000000
        no_dec = True
        j = 1
        # parse the array, find first point of decrease
        # mark it, after it's marked, you can look through array
        # if there's another decrease, False, else True
        if len(nums) < 2:
            return True
        while(no_dec == True and j < len(nums)):
            print(j)
            if nums[j-1] > nums[j]:
                # found it
                no_dec = False
                #print(nums[j-1])
                #print(nums[j])
                if j == len(nums) - 1:
                    nums[j] = -100000000
                elif nums[j-1] > nums[j+1]:
                    nums[j-1] = -100000000
                elif nums[j-1] <= nums[j+1]:
                    nums[j] = -100000000
                break
            j += 1
            #print("set")
        print(nums)
        for x in range(0, len(nums)):
            if nums[x] == -100000000:
                pass
            elif nums[x] < cur:
                return False
            else:
                cur = nums[x]
        return True
    
        