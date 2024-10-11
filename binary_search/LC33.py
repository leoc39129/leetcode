class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Base case: len(nums) == 1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        # The array will always be increasing EXCEPT for ONE point in the array
        # ex: [4,5,6,7,0,1,2] - you're increasing except for when you go from 7 to 0
        
        # The problem with binary search here is the array will possibly be unsorted
        # We have to do this in O(logn) complexity, so we can't resort it

        # How about - going from idx 0 to the right will ALWAYS be increasing,
        # while going left from idx len(nums) - 1 will be decreasing up to a point

        # What if we look from indices l=0 and r=len(nums)-1. 

        # If our target is less than nums[r], r -= 1
        # If we decreased from the previous number, good, keep going
        # If we didn't, that number will not be in nums

        # If our target is greater than nums[l], l += 1
        # If we increased from the previous number, good, keep going
        # If we didn't, that number will not be in nums

        # We know if the array is rotated or not -- just compare nums[l] and nums[r] at the beginning
        # If nums[l] < nums[r], we are unsorted -- run a normal binary search.
        # If nums[l] > nums[r], run our wonky search

        def bin_search(arr, target):
            print(arr)
            n = len(arr)
            print(n//2)
            if n == 0:
                return -1
                
            val = arr[n//2]
            if val == target:
                return n // 2
            elif val > target:
                # Repeat on the left half
                bin_search(arr[0:(n//2)], target)
            elif val < target:
                # Repeat on the right half
                return n//2 + bin_search(arr[(n//2)+1:], target)
            else:
                return -1

        l, r = 0, len(nums) - 1
        if nums[l] > nums[r]:
            while l != r:
                if target == nums[l]:
                    return l
                elif target == nums[r]:
                    return r
                elif target < nums[r]:
                    prev = nums[r]
                    r -= 1
                    if nums[r] > prev:
                        return -1
                elif target > nums[l]:
                    prev = nums[l]
                    l += 1
                    if nums[l] < prev:
                        return -1
                else:
                    return -1
        else:
            if len(nums) == 2:
                if nums[0] == target:
                    return 0
                elif nums[1] == target:
                    return 1
                else:
                    return -1
            else:
                bin_search(nums, target)
        return -1
    
'''
Almost got it, not quite there. Haven't done a binary search problem in a long time
so don't sweat it. Keep up the good work :)

Here's the corrected bin_search function. If that was correct, this solution would
be fully correct at O(logn) complexity

def bin_search(arr, target, start=0):
    n = len(arr)
    
    if n == 0:
        return -1

    mid = n // 2
    val = arr[mid]
    
    if val == target:
        return start + mid
    elif val > target:
        # Repeat on the left half and return the result
        return bin_search(arr[:mid], target, start)
    else:
        # Repeat on the right half and return the result, adjusting the start index
        result = bin_search(arr[mid+1:], target, start + mid + 1)
        return result if result != -1 else -1

Discussion Board Solution: Adjusted binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
'''