class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Base Case:
        if len(nums) == 1:
            return True
        if nums[0] > len(nums):
            return True
        
        idx = 0
        while idx < len(nums)-1:
            if nums[idx] == 0:
                # Backtrack to see if we can get past the zero
                count = 0
                for i in range(idx-1, -1, -1):
                    if nums[i] > idx - i:
                        idx += 1
                        break
                    else:
                        count += 1
                if count == idx:
                    return False
            else:
                idx += nums[idx]

        return True

        
'''
RT: O(n)
Space: O(1)

Good job identifying the keys of the problem -- only zeroes can stop you, and you can always
backtrack, so just be greedy and go as far as possible every time.

Here's a discussion board solution, thinking about the problem in a different way:

Basically, this solution ensures we're picking the best place to stop and "refill the gas
tank." In other words, look through it with the following example

[10,9,8,7,6,10,0,0,0,0,0,1,1,1]

We could use our max jump length at first, jumping from idx 0 to 10, but we'd land on a 0
This algorithm will choose to stop at idx 5, where nums[5] = 10, because between idx 1 and 10,
that is the best place to stop (i.e. -- you will get the furthest by stopping there). Say there was
a larger number directly after it...

[10,9,8,7,6,10,100,0,0,0,0,0,1,1,1]

We would still bump into that number on the following iteration, and choose that as the best "refilling"
spot. Clever solution!

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True


Here's a back to front approach -- see if you can reach the last index from the second to last index.
If you can't check the 3rd last index, then the 4th last index ...
If you can, reset the goal to be the second to last index, see if you can reach it from the third
to last index, rinse repeat.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False
'''