class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Base Case:
        n = len(height)
        if n < 3:
            return 0
        
        # Two Pointer Approach:
        # We look in "sections", where you increment r through a decreasing part of the window,
        # then through the increasing part of the window, basically to get the two local maxima 
        # of the window. Then, catch l up to r, adding how much water you'd be able to get by 
        # looking at those two maxima

        # So for the example shown, you start at l=0, r=1. You increment r until r=3, as that's
        # when you've seen both a decreasing then and increasing part of the window. The section
        # is from l=0 to r=3. Now, add the water. Since 0 is the smaller of the local maxima,
        # we add 0-0 to the water count. Increment l, now l=1, reset the smaller local maxima
        # which is now 1. Add to the water count, 1-1=0 (don't add anything). Rinse, repeat.

        def calc_section(l, r, height, count):
            # Return the amount of water that a section can hold
            print(l)
            print(r)
            local_max = min(height[r], height[l])
            for idx in range(l, r+1):
                count += local_max - height[idx]
                l += 1
            
            return count

        l, r = 0, 1
        count = 0

        increasing = False
        if height[l] > height[r]:
            decreasing = True
        else:
            decreasing = False
        
        while r < n:
            if r < n-1 and height[r+1] < height[r]:
                decreasing = True
            elif r < n-1 and height[r+1] > height[r]:
                increasing = True
            r += 1

            if increasing and decreasing:
                while r < n - 1 and height[r+1] >= height[r]:
                    r += 1
                increasing = False
                decreasing = False
                count = calc_section(l, r, height, count)
                l = r
            elif r == n - 1:
                # Prevents r from falling off the edge due to an incomplete
                # section at the end of the array, as in example 1 (l=10, r=11)
                count = calc_section(l, r, height, count)
                return count
        
        return count


'''
Damn close to a perfect solution. You did miss that you can skip all the way and set l equal to the first index
where height[n] > height[n+1]

Discussion board is filled with a bunch of solutions like the one below,
two pointers, starting with l=0, r=len(height)-1. It's an elegant solution, but I wonder if
my approach can still work. 

class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water
'''