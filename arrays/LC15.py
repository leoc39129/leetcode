class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []

        # Base Case: len(nums) >= 3
        if len(nums) == 3:
            if sum(nums) == 0:
                ret.append(nums)
                return ret

        nums.sort()
        
        # VERY brute force obviously
        # The problem is we need to look at unique doubles, and see if there's
        # a triplet to be made from that unique double
        # Maybe we track unique doubles?
        doubles = {}
        print(nums)
        prev = nums[1]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # for k in range(j+1, len(nums)):
                #     if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in ret:
                #         ret.append([nums[i], nums[j], nums[k]])
                val = -1*(nums[i]+nums[j])
                if val not in nums[j+1:len(nums)]:
                    continue
                elif [nums[i], nums[j], val] not in ret:
                    ret.append([nums[i], nums[j], val])

        return ret
        
'''
Runtime issues gets through 308/313 which makes sense

Take it one step further with the sorting!

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res
'''