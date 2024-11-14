class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            area = (right - left)*min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area

'''
RT: O(n)
Space: O(1)

I had done this problem before, but it's been a while so good job on figuring out
the optimal solution.
'''