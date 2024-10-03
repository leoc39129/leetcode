class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        
        sorted_nums = self.sortArr(nums)
        
        for start_idx in range(len(sorted_nums)):
            for end_idx in range(start_idx, len(sorted_nums)):
                ret.append(sorted_nums[start_idx:end_idx+1])

        return ret

    def sortArr(self, arr):
        # Base case: if the array has 1 or 0 elements, it's already sorted
        if len(arr) <= 1:
            return arr
        else:
            # Choose a pivot (can be any element, here we use the last one)
            pivot = arr[-1]
            # Separate the array into two parts:
            # - elements less than the pivot
            # - elements greater than or equal to the pivot
            less = [x for x in arr[:-1] if x <= pivot]
            greater = [x for x in arr[:-1] if x > pivot]
            # Recursively sort the two parts and concatenate them 
            return self.sortArr(less) + [pivot] + self.sortArr(greater)


# COME BACK TO THIS ONE
'''
Understand it more, come back to this
nums.sort()
        ans = [[]]
        memory = {i: 0 for i in set(nums)}
        print(memory)

        for i in nums:
            l = len(ans)
            print(l)
            for s in ans[memory[i]:l]: 
                ans.append(s+[i])
                print(ans)

            memory[i] = l
            print(memory)
        
        return ans
'''