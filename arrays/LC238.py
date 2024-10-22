class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Base Case:
        if len(nums) == 2:
            return [nums[1], nums[0]]

        ans = []
        ans_prod = 1
        for num in nums:
            ans_prod *= num
            ans.append(ans_prod)

        # Now ans is storing the prefix prods
        # Go from back to front, modifying nums to store the running suffix prods
        
        ans[-1] = ans[-2]
        for i in range(len(nums) - 2, -1, -1):
            ans[i] = nums[i+1]*ans[i-1]
            nums[i] = nums[i+1]*nums[i]
        ans[0] = nums[1]

        return ans
    
# RT: O(n)
# Space: "O(1)", problem states ans array doesn't count toward space complexity
# SEE FOLLOW UP: 
# Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

        

'''
Killed it! Great job. 

Initial solution after 30 mins, RT O(n), Space complexity O(n)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Base Case:
        if len(nums) == 2:
            return [nums[1], nums[0]]

        # Create a prefix and suffix product array (both O(n))
        prefix_prod = 1
        prefix = []
        suffix_prod = 1
        suffix = []

        for i in range(len(nums)):
            prefix_prod *= nums[i]
            suffix_prod *= nums[len(nums)-1-i]

            prefix.append(prefix_prod)
            suffix.append(suffix_prod)

        # print(suffix)
        # print(prefix)

        answer = []
        ans_prod = 1

        answer.append(suffix[-2])

        for k in range(1, len(nums) - 1):
            ans_prod = ans_prod * prefix[k-1] * suffix[len(nums) - 2 - k]
            answer.append(ans_prod)
            ans_prod = 1

        answer.append(prefix[-2])
        
        return answer

A different way of approaching the problem:

Initialize the output array to have all 1's, same size as nums
Multiply each value in output array by everything in nums to the left of it
Multiply each value in output array by everything in nums to the right of it

Simple and easy to read. Same RT and space as my solution.

class Solution:
    def productExceptSelf(self, nums):
        output = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
    
        return output        
'''

        


        