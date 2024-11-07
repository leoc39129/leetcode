class Solution:
    def rotate(self, nums, k):
        # Base Case:
        if len(nums) == 1:
            return nums

        k = k % len(nums)

        nums.reverse()
        nums = self.reverse(nums, 0, k-1)
        nums = self.reverse(nums, k, len(nums)-1)
        return nums

    def reverse(self, arr, start, stop):
        r = start
        l = stop

        while r < l:
            temp = arr[r]
            arr[r] = arr[l]
            arr[l] = temp
            r += 1
            l -= 1

        return arr

'''
RT: O(n)
Space: O(1)

Revisited this problem and kind of got a look before starting, but I figured it out. Below 
is a previously reviewed discussion board solution


class Solution:
    def rotate(self, nums, k):
        k %= len(nums)
        self.reverseArray(0, len(nums) - 1, nums)
        self.reverseArray(0, k - 1, nums)
        self.reverseArray(k, len(nums) - 1, nums)

    def reverseArray(self, left, right, array):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

'''