class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Base Case:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        nums_dict = {}
        for num in nums:
            nums_dict[num] = 1

        sequence = float('-inf')
        for key in nums_dict.keys():
            if key-1 in nums_dict:
                continue
            ctr = 1
            key_up = key
            sequence_on = True
            while sequence_on:
                if key_up+1 in nums_dict:
                    ctr += 1
                    key_up += 1
                else:
                    sequence_on = False
            if ctr > sequence:
                sequence = ctr

        if sequence == 0:
            return 1
        else:
            return sequence

            
'''
RT: O(n)
Space: O(n)

You can replace the dictionary with a set -- not sure why this is under HashMaps in LeetCode.
Good solution!

Here's GPT's solution:

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Convert the list to a set for O(1) lookups
        nums_set = set(nums)
        max_sequence = 0

        for num in nums_set:
            # Only start counting if `num` is the beginning of a sequence
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                # Count the length of the sequence
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                # Update max sequence length
                max_sequence = max(max_sequence, current_streak)

        return max_sequence

        
Here's a different approach from the discussion board

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        res = 0
        
        while nums_set:
            curr = 1
            num = nums_set.pop()
            lower = num - 1
            higher = num + 1
            while lower in nums_set:
                nums_set.remove(lower)
                lower -= 1
                curr += 1
            while higher in nums_set:
                nums_set.remove(higher)
                higher += 1
                curr += 1
            res = max(res, curr)

        return res
        
'''