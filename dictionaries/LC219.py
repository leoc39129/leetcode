class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Base Case:
        if len(nums) == 1:
            return False
        if k == 0:
            return False

        if len(set(nums)) == len(nums):
            return False

        num_dict = {}

        for idx in range(len(nums)):
            if nums[idx] not in num_dict.keys():
                num_dict[nums[idx]] = idx
            else:
                if idx - num_dict[nums[idx]] <= k:
                    return True
                else:
                    num_dict[nums[idx]] = idx

        # Sliding Window approach may work here, 
        # I was trying to do something like strings/LC30.py
        # Figured I'd use the dictionary, the whole point of the problem

        # for key in num_dict.keys():    
        #     for idx in range(len(num_dict[key]) - 1):
        #         if num_dict[key][idx + 1] -  num_dict[key][idx] <= k:
        #             return True
        # tracker = []

        # l, r = 0, 1

        # while r < len(nums) and r - l <= k:
        #     if nums[l] == nums[r]:
        #         return True
        #     elif nums[r] not in tracker:
        #         tracker.append(nums[r])
        #         r += 1

        return False

'''
So this code was failing on exceeding time until the third "base case" -- 
if there are no duplicate numbers, we can automatically return false even
if making a set of nums is an expensive operation for nums where 
len(nums) = 10**5

I knew this code was O(n) (worst case, we loop over nums once in its
entirety), but I'm not sure why we exceeded time limits without the third 
base case. Hasing collisions probably?

Remember we realized if k > len(nums) then we just need a duplicate?

    width = k + 1
    if width > len(nums):
        return len(set(nums)) < len(nums)

Here's a discussion board solution checking only k elements using a set:

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        width = k + 1
        if width > len(nums):
            return len(set(nums)) < len(nums)
        window = {nums[i] for i in range(width)}
        if len(window) < width:
            return True
        for i in range(width, len(nums)):
            window.remove(nums[i - width])
            window.add(nums[i])
            if len(window) < width:
                return True
        return False
'''